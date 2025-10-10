# Admin Guide - Dynamic Homepage Management

## 🎉 Your Homepage is Now Dynamic!

All photos and content on the homepage can now be managed from the Django admin panel.

## How to Access Admin Panel

1. **Start your server** (if not running):
   ```bash
   cd /Users/equacare/Documents/equacare
   source venv/bin/activate
   python manage.py runserver
   ```

2. **Go to**: http://127.0.0.1:8000/admin/

3. **Login** with your admin credentials

## Managing Homepage Sections

### 📸 Hero Section (Top Photo)

**Location in Admin**: `Hero Section`

**What you can change:**
- **Hero Image**: Upload your main hero background photo (Recommended: 1920x1080px)
- **Title**: Main headline text
- **Subtitle**: Description paragraph
- **Button 1**: Text and link for the first button (e.g., "Call Now")
- **Button 2**: Text and link for the second button (e.g., "Request Consultation")
- **Active Status**: Turn the section on/off

**How to add/edit:**
1. Click "Hero Section" in admin
2. Click "Add Hero Section" or edit existing
3. Upload your hero image
4. Fill in the text fields
5. Check "Is active" checkbox
6. Click "Save"

**Note**: Only ONE hero section can be active at a time. When you activate a new one, the old one automatically deactivates.

---

### 🏠 About Preview Section

**Location in Admin**: `About Preview Section`

**What you can change:**
- **Preview Image**: Upload image for about section (Recommended: 800x600px)
- **Section Label**: Small label text (e.g., "About Equacare")
- **Title**: Section headline
- **Content Paragraph 1**: First paragraph of text
- **Content Paragraph 2**: Second paragraph of text
- **Button Text**: Text for the button (e.g., "Learn More About Us")
- **Button Link**: Where the button goes (e.g., "/about/")
- **Active Status**: Turn the section on/off

**How to add/edit:**
1. Click "About Preview Section" in admin
2. Click "Add About Preview Section" or edit existing
3. Upload your preview image
4. Fill in all text fields
5. Check "Is active" checkbox
6. Click "Save"

**Note**: Only ONE about preview can be active at a time.

---

## 📁 Where Images Are Stored

All uploaded images are saved to:
- **Location**: `/Users/equacare/Documents/equacare/media/homepage/`
- **URL**: Automatically handled by Django

---

## 🔄 Fallback Content

If you haven't created Hero or About Preview sections in admin yet, the website will automatically show:
- Static images from `/static/images/`
- Default text content

This means your site will always work, even without admin content!

---

## 🎨 Image Recommendations

### Hero Image:
- **Size**: 1920x1080px (or similar landscape ratio)
- **Format**: JPG, PNG, or WebP
- **Content**: Wide-angle photo showing caregivers or home care scenes

### About Preview Image:
- **Size**: 800x600px
- **Format**: JPG, PNG, or WebP
- **Content**: Caregiver with senior, caring moments

---

## 🚀 Quick Steps to Get Started

1. Go to admin: http://127.0.0.1:8000/admin/
2. Click "Hero Section" → "Add Hero Section"
3. Upload your hero image
4. Fill in title, subtitle, buttons
5. Check "Is active"
6. Save
7. Repeat for "About Preview Section"
8. Visit homepage to see your changes!

---

## 💡 Tips

- **Test before going live**: Always preview changes on localhost first
- **Optimize images**: Use compressed images for faster loading
- **Backup**: Keep original images backed up elsewhere
- **Multiple versions**: You can create multiple versions and switch between them by toggling "Is active"

---

## Need Help?

If you need to add more dynamic sections or change other parts of the website, just ask!

