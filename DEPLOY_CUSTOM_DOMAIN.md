# 🚀 Quick Start: Deploy Equacare to Custom Domain

This is a simplified quick-start guide. For detailed instructions, see `CUSTOM_DOMAIN_GUIDE.md`.

---

## 📝 Prerequisites Checklist

- [ ] GitHub account (code must be pushed to GitHub)
- [ ] Custom domain purchased (or will purchase)
- [ ] Gmail App Password for equacare77@gmail.com

---

## 🎯 3-Step Deployment Process

### Step 1: Deploy to Render.com (FREE)

1. **Sign Up:** Go to https://render.com → Sign in with GitHub
2. **Create Web Service:** Click "New +" → "Web Service"
3. **Connect Repository:** Select your `equacare` repository
4. **Configure Settings:**
   ```
   Name: equacare
   Runtime: Python 3
   Build Command: ./build.sh
   Start Command: gunicorn equacare_project.wsgi:application
   Instance Type: Free
   ```
5. **Add Environment Variables:**
   ```
   PYTHON_VERSION = 3.9.18
   DEBUG = False
   SECRET_KEY = [generate using: python -c "import secrets; print(secrets.token_urlsafe(50))"]
   EMAIL_PASSWORD = [your Gmail App Password]
   ```
6. **Create PostgreSQL Database** (optional but recommended)
7. **Deploy!** Wait 5-10 minutes
8. **Test:** Visit your Render URL (e.g., `https://equacare.onrender.com`)

---

### Step 2: Purchase Domain

**Recommended Registrars:**
- **Namecheap** (https://www.namecheap.com) - Affordable, $10-15/year
- **Google Domains** (https://domains.google.com) - Simple interface
- **Cloudflare** (https://www.cloudflare.com/products/registrar/) - Best security

**Domain Ideas:**
- `equacare.com`
- `equacareservices.com`
- `equacarellc.com`

---

### Step 3: Connect Custom Domain

#### A. Add Domain in Render

1. Go to your Web Service in Render
2. Click **Settings** → **Custom Domain**
3. Click **Add Custom Domain**
4. Enter: `www.equacare.com` (or your domain)
5. Save

#### B. Configure DNS

Go to your domain registrar and add these DNS records:

**For www subdomain:**
```
Type: CNAME
Name: www
Value: equacare.onrender.com
```

**For root domain (optional):**
```
Type: A
Name: @
Value: [IP provided by Render]
```

Or use CNAME flattening:
```
Type: CNAME
Name: @
Value: equacare.onrender.com
```

#### C. Update Django Settings

Add environment variable in Render:
```
CUSTOM_DOMAIN = equacare.com,www.equacare.com
```

Or manually edit `settings.py`:
```python
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',
    'equacare.com',
    'www.equacare.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'https://equacare.com',
    'https://www.equacare.com',
]
```

Then push to GitHub:
```bash
git add .
git commit -m "Add custom domain"
git push origin main
```

#### D. Wait and Verify

1. **DNS Propagation:** Wait 15 minutes to 24 hours
2. **Check Status:** https://dnschecker.org
3. **Verify in Render:** Click "Verify" next to your domain
4. **SSL Auto-Provisioned:** HTTPS will be automatic

---

## 🎉 You're Live!

Visit your website at:
- `https://www.equacare.com`
- `https://equacare.com`

---

## ⚙️ Post-Deployment

### Create Admin User

In Render Dashboard → Shell tab:
```bash
python manage.py createsuperuser
```

### Add Content

1. Visit `https://yourdomain.com/admin/`
2. Login with superuser credentials
3. Add content:
   - Site Settings
   - Hero Section
   - Services
   - Job Listings

---

## 🐛 Quick Troubleshooting

**Domain not working?**
- Wait for DNS propagation (check https://dnschecker.org)
- Verify DNS records in your registrar
- Check ALLOWED_HOSTS in settings.py

**400 Bad Request?**
- Add domain to ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS
- Push changes to GitHub

**SSL not working?**
- Wait 15-30 minutes after domain verification
- Render auto-provisions SSL certificates

---

## 💰 Cost Summary

- **Domain:** $10-20/year
- **Hosting (Render Free):** $0/year
- **SSL Certificate:** FREE
- **Total:** ~$10-20/year

---

## 📚 More Help

- **Detailed Guide:** See `CUSTOM_DOMAIN_GUIDE.md`
- **Render Docs:** https://render.com/docs/web-services
- **Django Docs:** https://docs.djangoproject.com/en/4.2/howto/deployment/

---

**Questions?** Contact your developer or Render support.

**Good luck! 🚀**

