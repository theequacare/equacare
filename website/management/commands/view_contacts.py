from django.core.management.base import BaseCommand
from website.models import ContactMessage


class Command(BaseCommand):
    help = 'View recent contact form submissions'

    def add_arguments(self, parser):
        parser.add_argument(
            '--limit',
            type=int,
            default=10,
            help='Number of recent contacts to show (default: 10)'
        )

    def handle(self, *args, **options):
        limit = options['limit']
        contacts = ContactMessage.objects.all().order_by('-created_at')[:limit]
        
        if not contacts:
            self.stdout.write(
                self.style.WARNING('No contact form submissions found.')
            )
            return
        
        self.stdout.write(
            self.style.SUCCESS(f'Recent Contact Form Submissions (last {len(contacts)}):')
        )
        self.stdout.write('=' * 60)
        
        for contact in contacts:
            self.stdout.write(f"\n📧 {contact.name} ({contact.email})")
            self.stdout.write(f"📅 {contact.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            self.stdout.write(f"📞 Phone: {contact.phone or 'Not provided'}")
            self.stdout.write(f"📝 Subject: {contact.subject}")
            self.stdout.write(f"💬 Message: {contact.message[:100]}{'...' if len(contact.message) > 100 else ''}")
            self.stdout.write('-' * 40)
