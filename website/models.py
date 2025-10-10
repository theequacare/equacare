from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):
    """Model for storing contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Service(models.Model):
    """Model for services offered by Equacare"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """Model for client testimonials"""
    client_name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=100, help_text="e.g., 'Family Member', 'Client'")
    testimonial = models.TextField()
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"{self.client_name} - {self.rating} stars"


class Notice(models.Model):
    """Model for announcements and notices"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'

    def __str__(self):
        return self.title


class Document(models.Model):
    """Model for PDF documents and resources"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='documents/')
    category = models.CharField(max_length=100, choices=[
        ('forms', 'Forms'),
        ('policies', 'Policies'),
        ('guides', 'Guides'),
        ('other', 'Other'),
    ], default='other')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title


class HeroSection(models.Model):
    """Model for homepage hero section"""
    title = models.CharField(max_length=200, default="Caring Support When You Need It Most")
    subtitle = models.TextField(default="We know life can be challenging, and we're here to make it easier.")
    hero_image = models.ImageField(upload_to='homepage/', help_text="Recommended size: 1920x1080px")
    button_text_1 = models.CharField(max_length=100, default="Call Now: (515) 508-1556")
    button_link_1 = models.CharField(max_length=200, default="tel:+15155081556")
    button_text_2 = models.CharField(max_length=100, default="Request Free Consultation")
    button_link_2 = models.CharField(max_length=200, default="/contact/")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Section'

    def __str__(self):
        return f"Hero Section - {self.title}"

    def save(self, *args, **kwargs):
        # Ensure only one active hero section
        if self.is_active:
            HeroSection.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class AboutPreview(models.Model):
    """Model for homepage about preview section"""
    section_label = models.CharField(max_length=100, default="About Equacare")
    title = models.CharField(max_length=200, default="Flexible Care That Fits Your Life")
    content_paragraph_1 = models.TextField(default="Every family's needs are unique.")
    content_paragraph_2 = models.TextField(default="We match you with caregivers who understand your specific needs.")
    preview_image = models.ImageField(upload_to='homepage/', help_text="Recommended size: 800x600px")
    button_text = models.CharField(max_length=100, default="Learn More About Us")
    button_link = models.CharField(max_length=200, default="/about/")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About Preview Section'
        verbose_name_plural = 'About Preview Section'

    def __str__(self):
        return f"About Preview - {self.title}"

    def save(self, *args, **kwargs):
        # Ensure only one active about preview
        if self.is_active:
            AboutPreview.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

