"""
URL configuration for equacare_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Password Reset URLs
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(
        template_name='admin/password_reset_form.html',
        email_template_name='admin/password_reset_email.html',
        subject_template_name='admin/password_reset_subject.txt',
        success_url='/admin/password_reset/done/'
    ), name='admin_password_reset'),
    
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='admin/password_reset_done.html'
    ), name='password_reset_done'),
    
    path('admin/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='admin/password_reset_confirm.html',
        success_url='/admin/reset/complete/'
    ), name='password_reset_confirm'),
    
    path('admin/reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='admin/password_reset_complete.html'
    ), name='password_reset_complete'),
    
    path('', include('website.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

