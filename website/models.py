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


class ServicesHeader(models.Model):
    """Model for services section header on homepage"""
    section_label = models.CharField(max_length=100, default="Our Services")
    title = models.CharField(max_length=200, default="How We Can Help")
    subtitle = models.TextField(default="From a few hours a week to around-the-clock care, we're here with a helping hand")
    button_text = models.CharField(max_length=100, default="View All Services")
    button_link = models.CharField(max_length=200, default="/services/")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Services Section Header'
        verbose_name_plural = 'Services Section Header'

    def __str__(self):
        return f"Services Header - {self.title}"

    def save(self, *args, **kwargs):
        if self.is_active:
            ServicesHeader.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class ContactFormSection(models.Model):
    """Model for contact form section on homepage"""
    # Header
    title = models.CharField(max_length=200, default="Let Us Know What's On Your Mind")
    subtitle = models.TextField(default="Request a no-obligation, in-home consultation")
    
    # Form Field Labels
    name_label = models.CharField(max_length=100, default="Name:")
    email_label = models.CharField(max_length=100, default="Email:")
    phone_label = models.CharField(max_length=100, default="Phone:")
    subject_label = models.CharField(max_length=100, default="Subject:")
    message_label = models.CharField(max_length=100, default="Message:")
    
    # Subject Options (one per line)
    subject_options = models.TextField(
        default="Request Free Consultation\nGeneral Inquiry\nServices Information",
        help_text="Enter one subject option per line"
    )
    
    # Button & Messages
    submit_button_text = models.CharField(max_length=100, default="Send Message")
    success_message = models.TextField(default="Thank you for contacting us! We will get back to you soon.")
    error_message = models.TextField(default="An error occurred. Please try again or call us directly.")
    
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact Form Section'
        verbose_name_plural = 'Contact Form Section'

    def __str__(self):
        return f"Contact Form - {self.title}"
    
    def get_subject_options_list(self):
        """Return subject options as a list"""
        return [opt.strip() for opt in self.subject_options.split('\n') if opt.strip()]

    def save(self, *args, **kwargs):
        if self.is_active:
            ContactFormSection.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class CTASection(models.Model):
    """Model for CTA (Call to Action) section at bottom of homepage"""
    title = models.CharField(max_length=200, default="Ready to Talk?")
    subtitle = models.TextField(default="It all starts with a conversation. Call us or send a message above.")
    button_text = models.CharField(max_length=100, default="Call Now: (515) 508-1556")
    button_link = models.CharField(max_length=200, default="tel:+15155081556")
    show_button = models.BooleanField(default=True, help_text="Show/hide the call button")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'CTA Section'
        verbose_name_plural = 'CTA Section'

    def __str__(self):
        return f"CTA - {self.title}"

    def save(self, *args, **kwargs):
        if self.is_active:
            CTASection.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class JobListing(models.Model):
    """Model for job/career listings"""
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default="Urbandale, IA")
    job_type = models.CharField(max_length=50, choices=[
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('contract', 'Contract'),
        ('per-diem', 'Per Diem'),
    ], default='full-time')
    description = models.TextField(help_text="Brief job description")
    responsibilities = models.TextField(help_text="List main responsibilities (one per line)")
    qualifications = models.TextField(help_text="List required qualifications (one per line)")
    benefits = models.TextField(blank=True, help_text="List benefits (one per line)")
    salary_range = models.CharField(max_length=100, blank=True, help_text="e.g., $15-20/hour")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Job Listing'
        verbose_name_plural = 'Job Listings'
    
    def __str__(self):
        return f"{self.title} - {self.location}"
    
    def get_responsibilities_list(self):
        """Return responsibilities as a list"""
        return [resp.strip() for resp in self.responsibilities.split('\n') if resp.strip()]
    
    def get_qualifications_list(self):
        """Return qualifications as a list"""
        return [qual.strip() for qual in self.qualifications.split('\n') if qual.strip()]
    
    def get_benefits_list(self):
        """Return benefits as a list"""
        if self.benefits:
            return [benefit.strip() for benefit in self.benefits.split('\n') if benefit.strip()]
        return []


class JobApplication(models.Model):
    """Model for job applications"""
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='applications')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    resume = models.FileField(upload_to='applications/', blank=True, null=True)
    cover_letter = models.TextField(blank=True)
    experience_years = models.IntegerField(default=0, help_text="Years of relevant experience")
    availability = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=[
        ('new', 'New'),
        ('reviewing', 'Reviewing'),
        ('interview', 'Interview Scheduled'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    ], default='new')
    notes = models.TextField(blank=True, help_text="Internal notes")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job.title}"


class AboutPage(models.Model):
    """Model for About page content"""
    # Header
    page_title = models.CharField(max_length=200, default="About Equacare")
    subtitle = models.CharField(max_length=300, default="Non-medical home care services for families in our community")
    
    # Content
    paragraph_1 = models.TextField(default="At Equacare, we understand that life can be challenging. That's why we provide compassionate, non-medical home care services to help you or your loved ones live comfortably and independently at home.")
    paragraph_2 = models.TextField(default="Our trained caregivers assist with everyday activities like personal care, meal preparation, light housekeeping, and companionship. We don't provide medical treatments or nursing care - we focus on the personal support that makes daily life easier.")
    
    # Image
    about_image = models.ImageField(upload_to='about/', help_text="Recommended size: 800x600px")
    
    # CTA Section
    cta_title = models.CharField(max_length=200, default="Ready to Learn More?")
    cta_text = models.TextField(default="Let's talk about how we can help you or your loved ones.")
    button_text = models.CharField(max_length=100, default="Contact Us")
    
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'About Page'
        verbose_name_plural = 'About Page'
    
    def __str__(self):
        return f"About Page - {self.page_title}"
    
    def save(self, *args, **kwargs):
        if self.is_active:
            AboutPage.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class SiteSettings(models.Model):
    """Model for site-wide contact information and settings"""
    # Company Info
    company_name = models.CharField(max_length=200, default="Equacare LLC")
    tagline = models.CharField(max_length=300, default="Professional Non-Medical Home Care Services", blank=True)
    
    # Contact Information
    phone = models.CharField(max_length=20, default="(515) 508-1556")
    phone_link = models.CharField(max_length=20, default="+15155081556", help_text="Phone number for tel: links (no spaces or dashes)")
    email = models.EmailField(default="equacare77@gmail.com")
    
    # Address
    street_address = models.CharField(max_length=200, default="7611 Douglas Ave #24")
    city = models.CharField(max_length=100, default="Urbandale")
    state = models.CharField(max_length=2, default="IA")
    zip_code = models.CharField(max_length=20, default="50322-3076")
    
    # Hours/Availability
    availability_text = models.CharField(max_length=100, default="Available 24/7")
    
    # Social Media (optional)
    facebook_url = models.URLField(blank=True, help_text="Full Facebook page URL")
    twitter_url = models.URLField(blank=True, help_text="Full Twitter profile URL")
    linkedin_url = models.URLField(blank=True, help_text="Full LinkedIn page URL")
    instagram_url = models.URLField(blank=True, help_text="Full Instagram profile URL")
    
    # Footer Text
    footer_about = models.TextField(
        default="Equacare LLC provides compassionate non-medical home care services to families in our community.",
        help_text="Brief description for footer"
    )
    copyright_text = models.CharField(
        max_length=200, 
        default="© 2024 Equacare LLC. All rights reserved.",
        help_text="Copyright text in footer"
    )
    
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return f"Site Settings - {self.company_name}"
    
    def get_full_address(self):
        """Return formatted full address"""
        return f"{self.street_address}, {self.city}, {self.state} {self.zip_code}"
    
    def get_address_lines(self):
        """Return address as separate lines for display"""
        return {
            'line1': self.street_address,
            'line2': f"{self.city}, {self.state} {self.zip_code}"
        }

    def save(self, *args, **kwargs):
        if self.is_active:
            SiteSettings.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

