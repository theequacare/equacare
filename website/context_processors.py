"""
Context processors for website app
Makes certain data available to all templates
"""
from .models import SiteSettings


def site_settings(request):
    """
    Add site settings to all template contexts
    """
    settings = SiteSettings.objects.filter(is_active=True).first()
    return {
        'site_settings': settings
    }

