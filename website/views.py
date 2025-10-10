from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Service, Testimonial, ContactMessage
import json


def home(request):
    """Home page view"""
    services = Service.objects.filter(is_active=True)[:6]
    testimonials = Testimonial.objects.filter(is_featured=True)[:3]
    
    context = {
        'services': services,
        'testimonials': testimonials,
    }
    return render(request, 'website/home.html', context)


def about(request):
    """About page view"""
    return render(request, 'website/about.html')


def services(request):
    """Services page view"""
    services = Service.objects.filter(is_active=True)
    context = {
        'services': services,
    }
    return render(request, 'website/services.html', context)


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
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for contacting us! We will get back to you soon.'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'An error occurred. Please try again later.'
        }, status=500)

