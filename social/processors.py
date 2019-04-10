from .models import Link

def contex_dict(request):
    contex = {}
    links = Link.objects.all()
    for link in links:
        contex[link.key] = link.url
    return contex