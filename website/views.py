from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import ContactMessage, JobApplication
import json
import logging

logger = logging.getLogger(__name__)


def home(request):
    """Home page view"""
    from .models import HeroSection, AboutPreview, ServicesHeader, ContactFormSection, CTASection
    
    hero = HeroSection.objects.filter(is_active=True).first()
    about_preview = AboutPreview.objects.filter(is_active=True).first()
    services_header = ServicesHeader.objects.filter(is_active=True).first()
    contact_form_section = ContactFormSection.objects.filter(is_active=True).first()
    cta_section = CTASection.objects.filter(is_active=True).first()
    
    context = {
        'hero': hero,
        'about_preview': about_preview,
        'services_header': services_header,
        'contact_form_section': contact_form_section,
        'cta_section': cta_section,
    }
    return render(request, 'website/home.html', context)


def about(request):
    """About page view"""
    from .models import AboutPage, CEOSection, ProgramGallery
    
    about_page = AboutPage.objects.filter(is_active=True).first()
    ceo_section = CEOSection.objects.filter(is_active=True).first()
    gallery_photos = ProgramGallery.objects.filter(is_active=True)
    context = {
        'about_page': about_page,
        'ceo_section': ceo_section,
        'gallery_photos': gallery_photos,
    }
    return render(request, 'website/about.html', context)


def services(request):
    """Services page view"""
    return render(request, 'website/services.html')


def knowledge(request):
    """Knowledge Center page view"""
    from .models import Notice, Document
    
    notices = Notice.objects.filter(is_active=True)
    documents = Document.objects.filter(is_active=True)
    
    context = {
        'notices': notices,
        'documents': documents,
    }
    return render(request, 'website/knowledge.html', context)


def contact(request):
    """Contact page view"""
    return render(request, 'website/contact.html')


@require_http_methods(["POST"])
def submit_contact(request):
    """Handle contact form submission via AJAX"""
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        # Validation
        if not all([name, email, subject, message]):
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all required fields.'
            }, status=400)
        
        # Save to database
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        
        # Send email notification
        try:
            # Check if email is properly configured
            if not settings.EMAIL_HOST_PASSWORD:
                logger.warning("Email not configured - contact form submission saved to database only")
            else:
                email_subject = f'New Contact Form Submission: {subject}'
                email_body = f"""
New contact form submission from Equacare website:

Name: {name}
Email: {email}
Phone: {phone}
Subject: {subject}

Message:
{message}

---
This is an automated notification from your Equacare website.
                """
                
                send_mail(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=True,
                )
                logger.info(f"Contact form email sent successfully for: {name}")
        except Exception as e:
            # Log error but don't fail the request
            logger.error(f"Failed to send contact form email: {e}")
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for contacting us! We will get back to you soon.'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'An error occurred. Please try again later.'
        }, status=500)


def careers(request):
    """Careers page view"""
    from .models import CareerPage, CareerNotice
    career_page = CareerPage.objects.filter(is_active=True).first()
    career_notices = CareerNotice.objects.filter(is_active=True)
    context = {
        'career_page': career_page,
        'career_notices': career_notices,
    }
    return render(request, 'website/careers.html', context)


@require_http_methods(["POST"])
def submit_application(request):
    """Handle general job application submission"""
    try:
        # Get form data
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()
        cover_letter = request.POST.get('cover_letter', '').strip()
        experience_years = request.POST.get('experience_years', 0)
        availability = request.POST.get('availability', '').strip()
        resume = request.FILES.get('resume')
        
        # Validation
        if not all([first_name, last_name, email, phone]):
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all required fields.'
            }, status=400)
        
        # Save application
        application = JobApplication.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            cover_letter=cover_letter,
            experience_years=int(experience_years) if experience_years else 0,
            availability=availability,
            resume=resume
        )
        
        # Send email notification with resume (optional - won't fail if email not configured)
        try:
            # Only send email if properly configured
            if settings.EMAIL_HOST_PASSWORD:
                email_subject = f'New Job Application - {first_name} {last_name}'
                email_body = f"""
New general job application received from Equacare website:

Applicant: {first_name} {last_name}
Email: {email}
Phone: {phone}
Address: {address}
Experience: {experience_years} years
Availability: {availability}

Cover Letter:
{cover_letter}

The resume is attached to this email.

View full application in admin panel:
http://127.0.0.1:8000/admin/website/jobapplication/{application.id}/change/

---
This is an automated notification from your Equacare website.
                """
                
                # Create email with attachment
                email_message = EmailMessage(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                )
                
                # Attach resume if provided
                if resume:
                    email_message.attach(resume.name, resume.read(), resume.content_type)
                
                email_message.send(fail_silently=True)
                logger.info(f"Job application email sent for: {first_name} {last_name}")
            else:
                logger.info(f"Job application saved (email not configured): {first_name} {last_name}")
        except Exception as e:
            # Log error but don't fail the request
            logger.error(f"Failed to send job application email: {e}")
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for your application! We will review it and get back to you soon.'
        })
        
    except JobListing.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Job listing not found. This position may no longer be available.'
        }, status=404)
    except Exception as e:
        logger.error(f"Job application error: {str(e)}", exc_info=True)
        return JsonResponse({
            'success': False,
            'message': f'An error occurred: {str(e)}. Please try again later.'
        }, status=500)

