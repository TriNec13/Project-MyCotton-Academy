# frontend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog, name='Blog'),
    path('/login', views.Login, name='Login'),
    path('/about', views.About, name='About'),
    path('/contact', views.Contact, name='Contact'),
]
