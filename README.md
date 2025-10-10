# Equacare LLC - Professional Home Care Website

A professional, modern website for Equacare LLC, a non-medical home care agency. Built with Django (Python backend) and JavaScript (frontend interactions).

## Features

- **Professional Design**: Modern, healthcare-focused design with smooth animations
- **Responsive**: Fully responsive design that works on all devices
- **Django Backend**: Robust Python/Django backend with admin panel
- **Interactive Frontend**: JavaScript-powered interactivity and smooth user experience
- **Contact Form**: AJAX-powered contact form with validation
- **Services Management**: Admin-manageable services and testimonials
- **SEO Optimized**: Proper meta tags and semantic HTML

## Technologies Used

- **Backend**: Django 4.2+ (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Database**: SQLite (development), PostgreSQL ready
- **Fonts**: Google Fonts (Poppins, Playfair Display)
- **Icons**: Font Awesome 6.4

## Project Structure

```
equacare/
├── equacare_project/       # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── website/                # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   └── admin.py           # Admin configuration
├── templates/             # HTML templates
│   └── website/
│       ├── base.html
│       ├── home.html
│       ├── about.html
│       ├── services.html
│       └── contact.html
├── static/                # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── manage.py
├── requirements.txt
└── README.md
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   cd /Users/equacare/Documents/equacare
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the website**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Admin Panel

Access the Django admin panel to manage:
- Contact form submissions
- Services offered
- Client testimonials

Login at `/admin/` with your superuser credentials.

## Customization

### Updating Contact Information

Edit the contact information in `templates/website/base.html` (footer section) and `templates/website/contact.html`.

### Adding Services

1. Log in to the admin panel
2. Navigate to Services
3. Add new services with title, description, and Font Awesome icon class

### Adding Testimonials

1. Log in to the admin panel
2. Navigate to Testimonials
3. Add client testimonials and mark as featured to display on homepage

### Styling

All styles are in `static/css/style.css`. CSS variables at the top of the file allow easy color customization.

## Deployment

### Environment Variables

Create a `.env` file with:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Production Checklist

- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Set up a production database (PostgreSQL recommended)
- [ ] Configure static files serving (WhiteNoise included)
- [ ] Set up HTTPS/SSL certificate
- [ ] Configure email backend for contact form notifications

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

© 2025 Equacare LLC. All rights reserved.

## Support

For questions or support, please contact:
- Email: dipakcalif@gmail.com
- Phone: (515) 508-1556
- Address: 7611 Douglas Ave #24, Urbandale, IA 50322-3076

---

Built with ❤️ for Equacare LLC

