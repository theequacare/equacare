# Admin Guide - Complete Homepage Management

## 🎉 Your ENTIRE Homepage is Now 100% Dynamic!

Every section, photo, and text on the homepage can be managed from the Django admin panel. No code changes needed!

---

## How to Access Admin Panel

1. **Start your server** (if not running):
   ```bash
   cd /Users/equacare/Documents/equacare
   source venv/bin/activate
   python manage.py runserver
   ```

2. **Go to**: http://127.0.0.1:8000/admin/

3. **Login**:
   - Username: `admin`
   - Password: `Nayakam@123`

---

## 📋 All Dynamic Sections on Homepage

### 1. 📸 Hero Section (Top Banner)

**Location in Admin**: `Hero Section`

**What you can manage:**
- ✅ **Hero Image**: Main background photo (1920x1080px recommended)
- ✅ **Title**: Main headline text
- ✅ **Subtitle**: Description paragraph
- ✅ **Button 1 Text & Link**: First call-to-action button
- ✅ **Button 2 Text & Link**: Second call-to-action button
- ✅ **Active Status**: Turn on/off

**Example:**
- Title: "Caring Support When You Need It Most"
- Subtitle: "We know life can be challenging..."
- Button 1: "Call Now: (515) 508-1556" → tel:+15155081556
- Button 2: "Request Free Consultation" → /contact/

---

### 2. 🏠 About Preview Section

**Location in Admin**: `About Preview Section`

**What you can manage:**
- ✅ **Preview Image**: About section photo (800x600px recommended)
- ✅ **Section Label**: Small text above title (e.g., "About Equacare")
- ✅ **Title**: Section headline
- ✅ **Content Paragraph 1 & 2**: Two paragraphs of text
- ✅ **Button Text & Link**: Link to full about page
- ✅ **Active Status**: Turn on/off

**Example:**
- Label: "About Equacare"
- Title: "Flexible Care That Fits Your Life"
- Button: "Learn More About Us" → /about/

---

### 3. 🛠️ Services Section Header

**Location in Admin**: `Services Section Header`

**What you can manage:**
- ✅ **Section Label**: Small text above title (e.g., "Our Services")
- ✅ **Title**: Section headline
- ✅ **Subtitle**: Description below title
- ✅ **Button Text & Link**: Link to full services page
- ✅ **Active Status**: Turn on/off

**Example:**
- Label: "Our Services"
- Title: "How We Can Help"
- Subtitle: "From a few hours a week to around-the-clock care..."
- Button: "View All Services" → /services/

**Note**: The actual services (Homemaking, Aide Services, etc.) are managed separately in the "Services" section.

---

### 4. 💼 Services (Individual Service Cards)

**Location in Admin**: `Services`

**What you can manage:**
- ✅ **Title**: Service name
- ✅ **Description**: Service details
- ✅ **Icon**: Font Awesome icon class (e.g., "fas fa-home")
- ✅ **Order**: Display order (lower numbers appear first)
- ✅ **Active Status**: Show/hide service

**Example Services:**
- Homemaking (fas fa-home)
- Aide Services (fas fa-hands-helping)
- Companionship (fas fa-user-friends)

---

### 5. 📝 Contact Form Section Header

**Location in Admin**: `Contact Form Section`

**What you can manage:**
- ✅ **Title**: Form headline
- ✅ **Subtitle**: Description text
- ✅ **Active Status**: Turn on/off

**Example:**
- Title: "Let Us Know What's On Your Mind"
- Subtitle: "Request a no-obligation, in-home consultation"

**Note**: The form fields themselves are fixed, but you can change the header text.

---

### 6. 📞 CTA Section (Bottom Call-to-Action)

**Location in Admin**: `CTA Section`

**What you can manage:**
- ✅ **Title**: CTA headline
- ✅ **Subtitle**: Description text
- ✅ **Show Button**: Toggle button visibility
- ✅ **Button Text & Link**: Call button customization
- ✅ **Active Status**: Turn on/off

**Example:**
- Title: "Ready to Talk?"
- Subtitle: "It all starts with a conversation..."
- Button: "Call Now: (515) 508-1556" → tel:+15155081556
- Show Button: ✓ (checked)

---

## 🚀 Quick Start Guide

### Step 1: Setup All Homepage Sections

1. Go to admin: http://127.0.0.1:8000/admin/
2. Add content for each section:
   - Click section name → "Add" button
   - Fill in all fields
   - Upload images (for Hero & About Preview)
   - Check "Is active"
   - Save

### Step 2: Add Your Services

1. Click "Services"
2. Add each service (Homemaking, Aide Services, etc.)
3. Set order numbers (1, 2, 3...)
4. Add Font Awesome icon classes
5. Save

### Step 3: View Your Dynamic Homepage

Visit: http://127.0.0.1:8000/

All changes appear instantly!

---

## 📁 Image Upload Locations

All uploaded images are saved to:
- **Directory**: `/Users/equacare/Documents/equacare/media/homepage/`
- **URL**: Automatically handled by Django

---

## 🎨 Image Recommendations

### Hero Image:
- **Size**: 1920x1080px (landscape)
- **Format**: JPG, PNG, or WebP
- **Content**: Wide-angle caregiving scenes

### About Preview Image:
- **Size**: 800x600px
- **Format**: JPG, PNG, or WebP
- **Content**: Caregiver with client, warm moments

---

## 🔄 How to Switch Content

You can create multiple versions of each section and switch between them:

1. Create new version (e.g., "Hero Section - Holiday")
2. Leave "Is active" unchecked
3. When ready to switch:
   - Edit the new version
   - Check "Is active"
   - Save
4. The old version automatically deactivates

---

## 💡 Pro Tips

### Fallback Content
- If no admin content is set, the site shows default static content
- This means your site always works!

### Testing
- Always test changes on localhost before deploying
- Use "Is active" checkbox to show/hide sections

### Multiple Admins
- You can create multiple admin accounts
- Each can manage content independently

### Icons
Use Font Awesome classes:
- Home: `fas fa-home`
- Helping: `fas fa-hands-helping`
- People: `fas fa-user-friends`
- Heart: `fas fa-heart`
- Medical: `fas fa-medkit`

Full list: https://fontawesome.com/icons

---

## 📊 What's Managed Where

| Homepage Section | Admin Panel Section | Upload Images? |
|-----------------|-------------------|---------------|
| Hero Banner | Hero Section | ✅ Yes |
| About Preview | About Preview Section | ✅ Yes |
| Services Header | Services Section Header | ❌ No |
| Service Cards | Services | ❌ No (icons only) |
| Contact Form Header | Contact Form Section | ❌ No |
| Bottom CTA | CTA Section | ❌ No |

---

## 🆘 Troubleshooting

### Images not showing?
- Hard refresh: `Cmd + Shift + R` (Mac) or `Ctrl + Shift + R` (Windows)
- Check "Is active" is checked
- Verify image uploaded successfully

### Changes not appearing?
- Clear browser cache
- Check correct section is "Is active"
- Restart server if needed

### Multiple sections active?
- Only ONE section of each type can be active
- Activating a new one automatically deactivates the old

---

## 📧 Other Admin Features

### Contact Messages
- View all contact form submissions
- Mark as read/unread
- Search by name, email, subject

### Knowledge Center
- **Notices**: Add announcements
- **Documents**: Upload PDF files for clients

### Testimonials
- Add client testimonials (if needed)
- Feature specific testimonials

---

## 🎯 Summary

✅ **Hero Section** - Banner photo + text + buttons  
✅ **About Preview** - About photo + content  
✅ **Services Header** - Services section title  
✅ **Services** - Individual service cards  
✅ **Contact Form** - Form header text  
✅ **CTA Section** - Bottom call-to-action  

**Everything is customizable without touching code!**

---

## 📞 Need Help?

If you need to:
- Add more sections
- Change layouts
- Add new features
- Customize further

Just ask! 😊
