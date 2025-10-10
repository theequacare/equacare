from django.contrib import admin
from .models import ContactMessage, Service, Testimonial


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    list_editable = ('order', 'is_active')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'relationship', 'rating', 'is_featured', 'created_at')
    list_filter = ('rating', 'is_featured', 'created_at')
    search_fields = ('client_name', 'testimonial')
    list_editable = ('is_featured',)
    date_hierarchy = 'created_at'

