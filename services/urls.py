from django.urls import path
from . import views as services_views

urlpatterns = [
   
    path('',services_views.services, name="services")

]
   