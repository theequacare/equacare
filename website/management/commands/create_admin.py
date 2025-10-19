from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Create admin user for production deployment'

    def handle(self, *args, **options):
        try:
            # Check if admin user already exists
            if User.objects.filter(username='admin').exists():
                admin_user = User.objects.get(username='admin')
                # Ensure password is correct even if user exists
                admin_user.set_password('Dhangadi$579')
                admin_user.is_staff = True
                admin_user.is_superuser = True
                admin_user.save()
                self.stdout.write(
                    self.style.SUCCESS('Admin user updated successfully!')
                )
                logger.info('Admin user updated with correct password')
            else:
                # Create admin user
                admin_user = User.objects.create_user(
                    username='admin',
                    email='admin@equacare.com',
                    password='Dhangadi$579',
                    is_staff=True,
                    is_superuser=True
                )
                self.stdout.write(
                    self.style.SUCCESS('Admin user created successfully!')
                )
                logger.info('Admin user created successfully')
            
            self.stdout.write('Username: admin')
            self.stdout.write('Password: Dhangadi$579')
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating admin user: {e}')
            )
            logger.error(f'Error creating admin user: {e}')
            raise
