#!/usr/bin/env python
"""
Manual script to create admin user for production
Run this if the Django management command fails
"""
import os
import sys
import django

# Add the project directory to Python path
sys.path.append('/Users/equacare/equacare-1')

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'equacare_project.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin():
    try:
        # Check if admin user already exists
        if User.objects.filter(username='admin').exists():
            admin_user = User.objects.get(username='admin')
            admin_user.set_password('admin123')
            admin_user.is_staff = True
            admin_user.is_superuser = True
            admin_user.save()
            print("✅ Admin user updated successfully!")
        else:
            # Create admin user
            admin_user = User.objects.create_user(
                username='admin',
                email='admin@equacare.com',
                password='admin123',
                is_staff=True,
                is_superuser=True
            )
            print("✅ Admin user created successfully!")
        
        print("Username: admin")
        print("Password: admin123")
        
    except Exception as e:
        print(f"❌ Error creating admin user: {e}")
        return False
    
    return True

if __name__ == "__main__":
    create_admin()
