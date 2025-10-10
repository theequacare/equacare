from django.contrib import admin
from .models import (
    ContactMessage, Service, Testimonial, Notice, Document, 
    HeroSection, AboutPreview, ServicesHeader, ContactFormSection, CTASection, SiteSettings
)


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


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'content')
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    readonly_fields = ('updated_at',)
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'hero_image')
        }),
        ('Buttons', {
            'fields': ('button_text_1', 'button_link_1', 'button_text_2', 'button_link_2')
        }),
        ('Status', {
            'fields': ('is_active', 'updated_at')
        }),
    )


@admin.register(AboutPreview)
class AboutPreviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    readonly_fields = ('updated_at',)
    fieldsets = (
        ('Content', {
            'fields': ('section_label', 'title', 'content_paragraph_1', 'content_paragraph_2', 'preview_image')
        }),
        ('Button', {
            'fields': ('button_text', 'button_link')
        }),
        ('Status', {
            'fields': ('is_active', 'updated_at')
        }),
    )


@admin.register(ServicesHeader)
class ServicesHeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    readonly_fields = ('updated_at',)
    fieldsets = (
        ('Content', {
            'fields': ('section_label', 'title', 'subtitle')
        }),
        ('Button', {
            'fields': ('button_text', 'button_link')
        }),
        ('Status', {
            'fields': ('is_active', 'updated_at')
        }),
    )


@admin.register(ContactFormSection)
class ContactFormSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    readonly_fields = ('updated_at',)
    fieldsets = (
        ('Header', {
            'fields': ('title', 'subtitle')
        }),
        ('Form Field Labels', {
            'fields': ('name_label', 'email_label', 'phone_label', 'subject_label', 'message_label'),
            'description': 'Customize the labels for each form field'
        }),
        ('Subject Dropdown Options', {
            'fields': ('subject_options',),
            'description': 'Enter one subject option per line. Example:\nRequest Free Consultation\nGeneral Inquiry\nServices Information'
        }),
        ('Button & Messages', {
            'fields': ('submit_button_text', 'success_message', 'error_message'),
            'description': 'Customize button text and form submission messages'
        }),
        ('Status', {
            'fields': ('is_active', 'updated_at')
        }),
    )


@admin.register(CTASection)
class CTASectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_button', 'is_active', 'updated_at')
    list_filter = ('is_active', 'show_button')
    readonly_fields = ('updated_at',)
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle')
        }),
        ('Button', {
            'fields': ('show_button', 'button_text', 'button_link')
        }),
        ('Status', {
            'fields': ('is_active', 'updated_at')
        }),
    )


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone', 'email', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    readonly_fields = ('updated_at',)
    fieldsets = (
        ('Company Information', {
            'fields': ('company_name', 'tagline')
        }),
        ('Contact Information', {
            'fields': ('phone', 'phone_link', 'email', 'availability_text'),
            'description': 'Main contact details shown throughout the site'
        }),
        ('Address', {
            'fields': ('street_address', 'city', 'state', 'zip_code'),
            'description': 'Physical address for your location'
        }),
        ('Social Media Links', {
            'fields': ('facebook_url', 'twitter_url', 'linkedin_url', 'instagram_url'),
            'description': 'Optional: Add your social media profile URLs',
            'classes': ('collapse',)
        }),
        ('Footer Content', {
            'fields': ('footer_about', 'copyright_text'),
            'description': 'Text displayed in the website footer'
        }),
        ('Status', {
            'fields': ('is_active', 'updated_at')
        }),
    )

