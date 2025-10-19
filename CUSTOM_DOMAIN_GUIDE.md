# 🌐 Custom Domain Deployment Guide for Equacare

This guide will help you deploy your Equacare website to your own custom domain (e.g., `equacare.com`, `www.equacare.com`).

---

## 📋 Overview

**Deployment Steps:**
1. Purchase a custom domain (if you don't have one)
2. Deploy your website to a hosting platform
3. Connect your custom domain to the hosting platform
4. Configure SSL/HTTPS

---

## 🛒 Step 1: Purchase a Domain

If you don't already have a domain, purchase one from:

### Recommended Domain Registrars:

1. **Namecheap** (https://www.namecheap.com)
   - ✅ Affordable (~$8-15/year)
   - ✅ Free WHOIS privacy
   - ✅ Easy DNS management

2. **Google Domains** (https://domains.google.com)
   - ✅ Simple interface
   - ✅ Free privacy protection
   - ✅ Integrated with Google services

3. **GoDaddy** (https://www.godaddy.com)
   - ✅ Popular and well-known
   - ✅ 24/7 support
   - ⚠️ More expensive

4. **Cloudflare Registrar** (https://www.cloudflare.com/products/registrar/)
   - ✅ At-cost pricing (no markup)
   - ✅ Free SSL and CDN
   - ✅ Best for security

**Domain Suggestions:**
- `equacare.com`
- `equacareservices.com`
- `equacarellc.com`
- `equacarehomecare.com`

**Cost:** Typically $10-20 per year

---

## 🚀 Step 2: Deploy to Hosting Platform

### Option A: Render.com (Recommended - FREE)

Render.com offers a free tier perfect for your Django website.

#### 2.1 Create Render Account

1. Go to **https://render.com**
2. Click **"Get Started"**
3. Sign up with your **GitHub account**

#### 2.2 Connect GitHub Repository

1. Make sure your code is pushed to GitHub
2. In Render Dashboard, click **"New +"** → **"Web Service"**
3. Connect your repository
4. Authorize Render to access it

#### 2.3 Configure Web Service

**Basic Settings:**
- **Name:** `equacare`
- **Region:** `Oregon (US West)` or closest to Iowa
- **Branch:** `main`
- **Runtime:** `Python 3`
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn equacare_project.wsgi:application`
- **Instance Type:** `Free`

#### 2.4 Add Environment Variables

Click **"Advanced"** and add:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.9.18` |
| `DEBUG` | `False` |
| `SECRET_KEY` | Generate a secure key (see below) |
| `EMAIL_PASSWORD` | Your Gmail App Password |

**To generate a secure SECRET_KEY:**
```python
# Run this in Python terminal:
import secrets
print(secrets.token_urlsafe(50))
```

#### 2.5 Create PostgreSQL Database (Optional but Recommended)

1. In Render, create a new **PostgreSQL** database
2. Name it `equacare_db`
3. Connect it to your web service
4. Render automatically sets the `DATABASE_URL` variable

#### 2.6 Deploy!

1. Click **"Create Web Service"**
2. Wait 5-10 minutes for deployment
3. You'll get a URL like: `https://equacare.onrender.com`

---

### Option B: Railway.app (Alternative - FREE with limitations)

1. Go to **https://railway.app**
2. Sign in with GitHub
3. Click **"New Project"** → **"Deploy from GitHub"**
4. Select your `equacare` repository
5. Railway auto-detects Django and deploys
6. Add environment variables in Settings
7. You'll get a URL like: `https://equacare.up.railway.app`

---

### Option C: DigitalOcean App Platform ($5/month)

Better performance but not free:

1. Go to **https://cloud.digitalocean.com/apps**
2. Click **"Create App"**
3. Connect your GitHub repository
4. Choose **Basic Plan** ($5/month)
5. Configure build and run commands
6. Deploy and get your URL

---

## 🔗 Step 3: Connect Custom Domain

Once your site is deployed, connect your custom domain:

### 3.1 Add Domain to Render (If using Render)

1. In Render Dashboard, go to your **Web Service**
2. Click **"Settings"** tab
3. Scroll to **"Custom Domain"** section
4. Click **"Add Custom Domain"**
5. Enter your domain (e.g., `www.equacare.com`)
6. Click **"Save"**

Render will show you DNS records to configure.

### 3.2 Configure DNS Records

Go to your domain registrar (Namecheap, GoDaddy, etc.) and add these DNS records:

#### For Root Domain (equacare.com):

**If using Render:**
| Type | Name | Value |
|------|------|-------|
| A | @ | Render's IP (they'll provide) |

**Alternative (using CNAME):**
| Type | Name | Value |
|------|------|-------|
| CNAME | @ | `equacare.onrender.com` |

#### For WWW subdomain (www.equacare.com):

| Type | Name | Value |
|------|------|-------|
| CNAME | www | `equacare.onrender.com` |

**Example for Namecheap:**
1. Log into Namecheap
2. Go to **Domain List** → Click **"Manage"** on your domain
3. Go to **Advanced DNS** tab
4. Click **"Add New Record"**
5. Add the records above

**DNS Propagation Time:** 5 minutes to 48 hours (usually ~1 hour)

### 3.3 Verify Domain

1. Wait for DNS propagation (check at https://dnschecker.org)
2. Back in Render, click **"Verify"** next to your custom domain
3. Once verified, Render automatically provisions a free SSL certificate

---

## 🔒 Step 4: Configure SSL/HTTPS

**Good news!** Render automatically provides free SSL certificates via Let's Encrypt.

Once your domain is verified:
- ✅ HTTPS is automatically enabled
- ✅ SSL certificate auto-renews
- ✅ HTTP redirects to HTTPS

**No additional configuration needed!**

---

## ⚙️ Step 5: Update Django Settings

Update your `settings.py` to allow your custom domain:

```python
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',
    'equacare.com',           # Add your domain
    'www.equacare.com',       # Add www version
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
    'https://*.up.railway.app',
    'https://*.onrender.com',
    'https://equacare.com',      # Add your domain
    'https://www.equacare.com',  # Add www version
]
```

**After updating:**
1. Commit changes: `git add .`
2. `git commit -m "Add custom domain to ALLOWED_HOSTS"`
3. `git push origin main`
4. Render will auto-deploy the updates

---

## 🎯 Step 6: Post-Deployment Setup

### Create Admin User

Access your site's shell (in Render, go to **Shell** tab):

```bash
python manage.py createsuperuser
```

Follow prompts:
- Username: `admin`
- Email: `equacare77@gmail.com`
- Password: (create a strong password)

### Add Content

1. Go to `https://yourdomain.com/admin/`
2. Login with superuser credentials
3. Add content:
   - **Site Settings** (contact info)
   - **Hero Section** (homepage)
   - **Services**
   - **Job Listings**
   - Upload images and documents

---

## ✅ Final Checklist

- [ ] Domain purchased and DNS configured
- [ ] Website deployed to Render/Railway
- [ ] Custom domain connected and verified
- [ ] SSL certificate active (HTTPS working)
- [ ] ALLOWED_HOSTS updated in settings.py
- [ ] Admin user created
- [ ] Site content added via admin panel
- [ ] All pages tested and working
- [ ] Email notifications tested
- [ ] Mobile responsiveness checked
- [ ] Contact form working

---

## 🔧 Troubleshooting

### Domain Not Working?

**Check DNS Propagation:**
- Go to https://dnschecker.org
- Enter your domain
- Verify DNS records are propagated globally

**Common Issues:**
- DNS not propagated yet (wait 1-24 hours)
- Wrong DNS records (double-check A/CNAME records)
- SSL not provisioned yet (wait 15-30 minutes after verification)

### "This site can't be reached" Error

1. Verify DNS records are correct
2. Check domain registrar settings
3. Ensure nameservers are correct
4. Wait for DNS propagation

### 400 Bad Request or CSRF Error

Update `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` in `settings.py` to include your domain.

### Images Not Loading

1. Run in Render Shell: `python manage.py collectstatic`
2. Upload images via Django admin panel
3. Check MEDIA_ROOT configuration

---

## 💰 Cost Breakdown

### Minimal Setup (Recommended)

- **Domain:** $10-20/year
- **Hosting (Render):** FREE
- **SSL Certificate:** FREE (auto-provided)
- **Total:** ~$10-20/year

### Production Setup

- **Domain:** $10-20/year
- **Hosting (DigitalOcean):** $5-12/month
- **Database:** Included with hosting
- **SSL Certificate:** FREE
- **Total:** ~$70-160/year

---

## 📚 Additional Resources

- **Render Docs:** https://render.com/docs
- **Django Deployment:** https://docs.djangoproject.com/en/4.2/howto/deployment/
- **DNS Configuration:** https://www.cloudflare.com/learning/dns/what-is-dns/
- **Let's Encrypt SSL:** https://letsencrypt.org/

---

## 🎉 Success!

Once everything is set up, your website will be live at:
- `https://equacare.com`
- `https://www.equacare.com`

With:
- ✅ Custom domain
- ✅ Free SSL/HTTPS
- ✅ Professional email forwarding (optional)
- ✅ Auto-deploy from GitHub
- ✅ 99.9% uptime

**Share your live website with the world!** 🌍

---

**Need help?** Contact your developer or reach out to Render support.

