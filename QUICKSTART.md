# Quick Start Guide - Equacare LLC Website

## 🎉 Your Professional Website is Ready!

A complete, professional website for Equacare LLC has been created with:
- ✅ Django backend (Python)
- ✅ JavaScript frontend with smooth interactions
- ✅ 4 main pages (Home, About, Services, Contact)
- ✅ Responsive design for all devices
- ✅ Admin panel for content management
- ✅ Contact form with AJAX submission
- ✅ Professional healthcare-focused design

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies

```bash
cd /Users/equacare/Documents/equacare

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Install requirements
pip install -r requirements.txt
```

### Step 2: Set Up Database

```bash
# Create database tables
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
# Follow prompts to create username and password
```

### Step 3: Run the Server

```bash
# Start development server
python manage.py runserver

# Open in browser:
# Website: http://127.0.0.1:8000/
# Admin: http://127.0.0.1:8000/admin/
```

## 📁 What's Included

### Pages
1. **Home** (`/`) - Hero section, features, services preview, testimonials
2. **About** (`/about/`) - Mission, vision, values, statistics
3. **Services** (`/services/`) - Detailed service descriptions, care plans
4. **Contact** (`/contact/`) - Contact form, location info

### Features
- Mobile-responsive navigation
- Smooth scroll animations
- Interactive service cards
- Contact form with validation
- Scroll-to-top button
- Professional color scheme
- Accessibility features

### Admin Panel
Access at `/admin/` to manage:
- **Services** - Add/edit/delete services
- **Testimonials** - Add/edit client testimonials
- **Contact Messages** - View form submissions

## 🎨 Customization

### Change Colors
Edit `static/css/style.css`, lines 27-48 (CSS variables):
```css
--primary-color: #2563eb;  /* Main blue */
--secondary-color: #10b981; /* Green */
```

### Update Contact Info
Edit these files:
- `templates/website/base.html` (footer)
- `templates/website/contact.html` (contact page)

### Add Your Logo
1. Add logo image to `static/images/`
2. Update `templates/website/base.html` line 30

### Add Photos
Place images in `static/images/`:
- `hero-bg.jpg` - Homepage hero background
- `about-preview.jpg` - Homepage about section
- `about-team.jpg` - About page
- `favicon.ico` - Browser tab icon

## 🔧 Common Tasks

### Add a New Service
1. Go to http://127.0.0.1:8000/admin/
2. Click "Services" > "Add Service"
3. Fill in details:
   - Title: "Personal Care"
   - Description: "Assistance with daily activities..."
   - Icon: "fas fa-hands-helping" (Font Awesome class)
   - Order: 1
4. Save

### Add a Testimonial
1. Go to admin panel > "Testimonials"
2. Click "Add Testimonial"
3. Check "Is Featured" to show on homepage
4. Save

### View Contact Form Submissions
1. Go to admin panel > "Contact Messages"
2. Click on any message to view details
3. Mark as read when reviewed

## 📤 Push to GitHub

See `DEPLOYMENT.md` for detailed instructions. Quick version:

```bash
# Option 1: Using GitHub CLI (easiest)
brew install gh
gh auth login
gh repo create equacare --private --source=. --push

# Option 2: Manual
# 1. Create repo at https://github.com/new
# 2. Then:
git remote set-url origin https://github.com/YOUR_USERNAME/equacare.git
git push -u origin main
```

## 🌐 Deploy to Production

Multiple options available:

1. **Railway.app** (Recommended - Easy)
   - Connect GitHub repo
   - Auto-deploys on push
   - Free tier available

2. **Heroku**
   - `heroku create equacare-app`
   - `git push heroku main`

3. **DigitalOcean App Platform**
   - Connect GitHub repo
   - Configure in dashboard

See `DEPLOYMENT.md` for detailed deployment instructions.

## 📱 Test Responsiveness

Test the website on:
- Desktop (Chrome, Firefox, Safari)
- Tablet (iPad, Android tablets)
- Mobile (iPhone, Android phones)

Or use browser DevTools:
1. Open website
2. Press F12 or Cmd+Option+I
3. Click device toggle button
4. Select different devices

## 🐛 Troubleshooting

### Port already in use
```bash
python manage.py runserver 8001
```

### Static files not loading
```bash
python manage.py collectstatic --noinput
```

### Database errors
```bash
# Reset database (WARNING: Deletes all data)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### CSS/JS changes not showing
- Hard refresh: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)
- Clear browser cache

## 📚 Documentation

- **README.md** - Project overview and setup
- **DEPLOYMENT.md** - Production deployment guide
- **QUICKSTART.md** - This file

## 🆘 Support Resources

- Django Docs: https://docs.djangoproject.com/
- Font Awesome Icons: https://fontawesome.com/icons
- CSS Variables: Edit `static/css/style.css`
- JavaScript: Edit `static/js/main.js`

## ✅ Project Structure

```
equacare/
├── equacare_project/    # Django settings
├── website/             # Main app (views, models, etc)
├── templates/           # HTML templates
├── static/              # CSS, JS, images
├── manage.py            # Django management
├── requirements.txt     # Python packages
└── README.md            # Documentation
```

## 🎯 Next Steps

1. ✅ Set up virtual environment
2. ✅ Install dependencies
3. ✅ Run migrations
4. ✅ Create superuser
5. ✅ Start server
6. 📝 Add your services in admin
7. 📝 Add your testimonials
8. 📝 Update contact information
9. 🎨 Add your photos
10. 🚀 Push to GitHub
11. 🌐 Deploy to production

---

## Need Help?

If you encounter any issues:
1. Check this guide first
2. Review README.md
3. Check Django documentation
4. Ensure virtual environment is activated
5. Verify all dependencies are installed

**Happy coding! Your professional home care website is ready to go! 🎉**

