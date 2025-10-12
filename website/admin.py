from django.contrib import admin
from .models import (
    ContactMessage, Service, Testimonial, Notice, Document, 
    HeroSection, AboutPreview, ServicesHeader, ContactFormSection, CTASection, SiteSettings,
    JobListing, JobApplication, AboutPage, CEOSection
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


@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'job_type', 'is_active', 'created_at')
    list_filter = ('job_type', 'is_active', 'created_at')
    search_fields = ('title', 'location', 'description')
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Job Information', {
            'fields': ('title', 'location', 'job_type', 'salary_range')
        }),
        ('Description', {
            'fields': ('description',),
            'description': 'Brief overview of the position'
        }),
        ('Responsibilities', {
            'fields': ('responsibilities',),
            'description': 'List main job responsibilities (one per line)'
        }),
        ('Qualifications', {
            'fields': ('qualifications',),
            'description': 'List required qualifications (one per line)'
        }),
        ('Benefits', {
            'fields': ('benefits',),
            'description': 'Optional: List benefits (one per line)'
        }),
        ('Status', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'job', 'email', 'phone', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'job')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    list_editable = ('status',)
    fieldsets = (
        ('Applicant Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'address')
        }),
        ('Job Details', {
            'fields': ('job', 'experience_years', 'availability')
        }),
        ('Application Materials', {
            'fields': ('resume', 'cover_letter'),
            'description': 'Resume upload and cover letter'
        }),
        ('Status & Notes', {
            'fields': ('status', 'notes', 'created_at')
        }),
    )


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    readonly_fields = ('updated_at',)
    fieldsets = (
        ('Page Header', {
            'fields': ('page_title', 'subtitle')
        }),
        ('Main Content', {
            'fields': ('paragraph_1', 'paragraph_2', 'about_image'),
            'description': 'Main about page content and image'
        }),
        ('CTA Section', {
            'fields': ('cta_title', 'cta_text', 'button_text'),
            'description': 'Call-to-action section at the bottom'
        }),
        ('Status', {
            'fields': ('is_active', 'updated_at')
        }),
    )


@admin.register(CEOSection)
class CEOSectionAdmin(admin.ModelAdmin):
    list_display = ('section_title', 'ceo_name', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    readonly_fields = ('updated_at',)
    fieldsets = (
        ('Section Header', {
            'fields': ('section_title',),
            'description': 'Title for the CEO section'
        }),
        ('CEO Information', {
            'fields': ('ceo_name', 'ceo_title', 'ceo_image'),
            'description': 'CEO name, title, and optional photo'
        }),
        ('Message Content', {
            'fields': ('paragraph_1', 'paragraph_2', 'paragraph_3', 'paragraph_4'),
            'description': 'CEO message divided into paragraphs for better readability'
        }),
        ('Signature', {
            'fields': ('closing_text', 'signature_name'),
            'description': 'Closing and signature (leave signature_name blank to use CEO name)'
        }),
        ('Status', {
            'fields': ('is_active', 'updated_at')
        }),
    )

