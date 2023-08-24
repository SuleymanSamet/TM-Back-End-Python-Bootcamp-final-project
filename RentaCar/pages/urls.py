from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('client/', views.client, name='client'),
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services'),
    path('chatbot/', views.chatbot, name='chatbot'),
]