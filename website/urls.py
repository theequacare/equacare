from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('knowledge/', views.knowledge, name='knowledge'),
    path('contact/', views.contact, name='contact'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
]

