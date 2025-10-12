from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create admin user for production deployment'

    def handle(self, *args, **options):
        # Check if admin user already exists
        if User.objects.filter(username='admin').exists():
            self.stdout.write(
                self.style.WARNING('Admin user already exists')
            )
            return

        # Create admin user
        admin_user = User.objects.create_user(
            username='admin',
            email='admin@equacare.com',
            password='admin123',
            is_staff=True,
            is_superuser=True
        )
        
        self.stdout.write(
            self.style.SUCCESS('Admin user created successfully!')
        )
        self.stdout.write('Username: admin')
        self.stdout.write('Password: admin123')
