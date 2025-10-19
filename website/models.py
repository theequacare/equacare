from django.db import models
from django.utils import timezone
import os


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
    """Model for documents and resources (supports all file formats)"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='documents/', help_text='Upload any file type: PDF, Word, Excel, PowerPoint, Images, etc.')
    category = models.CharField(max_length=100, choices=[
        ('forms', 'Forms'),
        ('policies', 'Policies'),
        ('guides', 'Guides'),
        ('other', 'Other'),
    ], default='other')
    access_type = models.CharField(max_length=20, choices=[
        ('download', 'Download'),
        ('view', 'View Only (Read-Only)'),
    ], default='download', help_text='Choose whether users can download or only view this document')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title
    
    def get_file_extension(self):
        """Get the file extension"""
        return os.path.splitext(self.file.name)[1].lower()
    
    def get_file_icon(self):
        """Return appropriate Font Awesome icon based on file type"""
        ext = self.get_file_extension()
        icon_map = {
            '.pdf': 'fa-file-pdf',
            '.doc': 'fa-file-word', '.docx': 'fa-file-word',
            '.xls': 'fa-file-excel', '.xlsx': 'fa-file-excel', '.csv': 'fa-file-excel',
            '.ppt': 'fa-file-powerpoint', '.pptx': 'fa-file-powerpoint',
            '.jpg': 'fa-file-image', '.jpeg': 'fa-file-image', '.png': 'fa-file-image',
            '.gif': 'fa-file-image', '.bmp': 'fa-file-image', '.svg': 'fa-file-image', '.webp': 'fa-file-image',
            '.zip': 'fa-file-archive', '.rar': 'fa-file-archive', '.7z': 'fa-file-archive',
            '.tar': 'fa-file-archive', '.gz': 'fa-file-archive',
            '.txt': 'fa-file-alt', '.rtf': 'fa-file-alt',
            '.mp4': 'fa-file-video', '.avi': 'fa-file-video', '.mov': 'fa-file-video',
            '.wmv': 'fa-file-video', '.flv': 'fa-file-video', '.mkv': 'fa-file-video',
            '.mp3': 'fa-file-audio', '.wav': 'fa-file-audio', '.ogg': 'fa-file-audio', '.m4a': 'fa-file-audio',
            '.html': 'fa-file-code', '.css': 'fa-file-code', '.js': 'fa-file-code',
            '.py': 'fa-file-code', '.java': 'fa-file-code', '.cpp': 'fa-file-code', '.c': 'fa-file-code',
        }
        return icon_map.get(ext, 'fa-file')
    
    def get_file_color(self):
        """Return color class based on file type"""
        ext = self.get_file_extension()
        color_map = {
            '.pdf': 'file-color-red',
            '.doc': 'file-color-blue', '.docx': 'file-color-blue',
            '.xls': 'file-color-green', '.xlsx': 'file-color-green', '.csv': 'file-color-green',
            '.ppt': 'file-color-orange', '.pptx': 'file-color-orange',
            '.jpg': 'file-color-purple', '.jpeg': 'file-color-purple', '.png': 'file-color-purple',
            '.gif': 'file-color-purple', '.bmp': 'file-color-purple', '.svg': 'file-color-purple', '.webp': 'file-color-purple',
            '.zip': 'file-color-yellow', '.rar': 'file-color-yellow', '.7z': 'file-color-yellow',
            '.tar': 'file-color-yellow', '.gz': 'file-color-yellow',
        }
        return color_map.get(ext, 'file-color-gray')


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


class CareerPage(models.Model):
    """Model for Career page header and intro content"""
    page_title = models.CharField(max_length=200, default="Careers")
    page_subtitle = models.CharField(max_length=300, default="Join a team that's about service, kindness, and respect")
    intro_paragraph_1 = models.TextField(default="Are you interested in working with us? Simply submit the application on this page. We'll review it now, and keep it on file for future openings.")
    intro_paragraph_2 = models.TextField(default="If you are the type of healthcare professional who takes pride in a job well done, our agency may be the right career move for you. We put the patient's needs first, but we also know that to give good service, you have to treat our caregivers well. Our first step in delivering excellent service to clients is to give the caregivers the support they need and the respect they deserve. If you would like to know about future job opportunities, simply use the form below to send your information.")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Career Page'
        verbose_name_plural = 'Career Page'

    def __str__(self):
        return self.page_title

    def save(self, *args, **kwargs):
        if self.is_active:
            CareerPage.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class CareerNotice(models.Model):
    """Model for career/hiring notices - simple notice-style announcements"""
    title = models.CharField(max_length=200, help_text="e.g., 'We're Hiring!', 'Join Our Team', 'Career Opportunities Available'")
    content = models.TextField(help_text="Description of available positions or hiring information")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Career Notice'
        verbose_name_plural = 'Career Notices'

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    """Model for job applications - all applications are general"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    best_time = models.CharField(max_length=200, blank=True, verbose_name="Best time to call")
    date_available = models.DateField(blank=True, null=True, verbose_name="Date available")
    degree_info = models.TextField(blank=True, verbose_name="Degree/Certification")
    other_certifications = models.TextField(blank=True, verbose_name="Other certifications")
    current_employment = models.CharField(max_length=300, blank=True, verbose_name="Current employment")
    employment_history = models.TextField(blank=True, verbose_name="Employment history")
    resume = models.FileField(upload_to='applications/', blank=True, null=True)
    general_comments = models.TextField(blank=True, verbose_name="General comments")
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
        return f"{self.first_name} {self.last_name} - General Application"


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


class CEOSection(models.Model):
    """Model for CEO section on About page"""
    section_title = models.CharField(max_length=200, default="A Message from Our CEO")
    ceo_name = models.CharField(max_length=200, default="[CEO Name]", help_text="Full name of the CEO")
    ceo_title = models.CharField(max_length=100, default="Chief Executive Officer")
    ceo_image = models.ImageField(upload_to='ceo/', blank=True, null=True, help_text="Optional: CEO photo (recommended size: 400x400px)")
    
    # Message paragraphs
    paragraph_1 = models.TextField(
        default="Welcome to Equacare LLC. We are truly honored that you have chosen us to be part of your care journey. At Equacare, our mission is to promote independence, dignity, comfort, and quality of life for each individual we serve."
    )
    paragraph_2 = models.TextField(
        default="Our team is dedicated to providing compassionate, reliable, and person-centered support in the comfort of your own home. We believe that with the right assistance, every person can enjoy the safety, familiarity, and meaningful connections of their home and community for as long as possible."
    )
    paragraph_3 = models.TextField(
        default="As a valued member, you are at the heart of everything we do. We are committed to respecting your rights, honoring your choices, and working closely with you and your family to support your unique needs and goals."
    )
    paragraph_4 = models.TextField(
        default="Thank you for placing your trust in Equacare LLC. We look forward to working together to make each day safe, comfortable, and meaningful."
    )
    
    # Signature/Closing
    closing_text = models.CharField(max_length=100, default="Warm regards,", help_text="Closing line before signature")
    signature_name = models.CharField(max_length=200, blank=True, help_text="Name for signature (leave blank to use CEO name)")
    
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'CEO Section'
        verbose_name_plural = 'CEO Section'
    
    def __str__(self):
        return f"CEO Section - {self.ceo_name}"
    
    def save(self, *args, **kwargs):
        if self.is_active:
            CEOSection.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class ProgramGallery(models.Model):
    """Model for program photos gallery on About page"""
    title = models.CharField(max_length=200, help_text="Title/name of the program or event")
    description = models.TextField(blank=True, help_text="Optional description of the program/event")
    photo = models.ImageField(upload_to='programs/', help_text="Program/event photo (recommended size: 800x600px)")
    date = models.DateField(blank=True, null=True, help_text="Date of the program/event (optional)")
    display_order = models.IntegerField(default=0, help_text="Order in which photos appear (lower numbers first)")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this photo from gallery")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Program Gallery Photo'
        verbose_name_plural = 'Program Gallery Photos'
        ordering = ['display_order', '-date', '-created_at']
    
    def __str__(self):
        return self.title


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

