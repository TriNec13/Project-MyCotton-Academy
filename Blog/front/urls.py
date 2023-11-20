from django.urls import path
from . import views

urlpatterns = [
    path('', views.front, name='front'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
