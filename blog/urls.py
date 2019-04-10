from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('',blog_views.blog, name="blog"),
    #category_id is String, but i want a number, how i can change to number? easy only add int:
    path('category/<int:category_id>/',blog_views.category, name="category"),

]