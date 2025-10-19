from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('knowledge/', views.knowledge, name='knowledge'),
    path('careers/', views.careers, name='careers'),
    path('contact/', views.contact, name='contact'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
    path('submit-application/', views.submit_application, name='submit_application'),
    # SEO
    path('sitemap.xml', views.sitemap, name='sitemap'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
]

