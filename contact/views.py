from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ConctactForm

# Create your views here.
def contact(request):
    contac_form = ConctactForm()

    if request.method == "POST":
        contac_form = ConctactForm(data=request.POST)
        if contac_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["xxxx@xxx.com"],
                reply_to=[email]

            )

            try:
                #if all is OK, send email and redirect
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                #something is wrong
                return redirect(reverse('contact')+"?fail")

            return redirect(reverse('contact')+"?ok")

    return render(request,"contact/contact.html", {'form':contac_form})