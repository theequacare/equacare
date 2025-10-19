# 🌐 Deploy Equacare to Your Custom Domain - START HERE

Welcome! This guide will help you deploy your Equacare website to an actual domain.

---

## 📚 Documentation Overview

I've created several guides for you:

### 1. **DEPLOY_CUSTOM_DOMAIN.md** ⭐ START HERE!
**Quick 3-step guide to deploy your site**
- Step 1: Deploy to Render.com (FREE hosting)
- Step 2: Purchase a domain
- Step 3: Connect your custom domain
- **Best for:** Quick setup, first-time deployment

### 2. **CUSTOM_DOMAIN_GUIDE.md**
**Comprehensive detailed guide**
- Complete walkthrough with screenshots descriptions
- Troubleshooting section
- Cost breakdowns
- Multiple hosting options
- **Best for:** Detailed reference, troubleshooting

### 3. **DEPLOYMENT_CHECKLIST.md**
**Interactive checklist**
- Print-friendly format
- Step-by-step checkboxes
- Credential tracking template
- Testing checklist
- **Best for:** Tracking your progress, making sure nothing is missed

---

## 🎯 Recommended Path

### For First-Time Deployment:

1. **Read:** `DEPLOY_CUSTOM_DOMAIN.md` (5-minute read)
2. **Follow:** The 3-step process
3. **Track Progress:** Use `DEPLOYMENT_CHECKLIST.md`
4. **Get Help:** Refer to `CUSTOM_DOMAIN_GUIDE.md` if stuck

---

## ⚡ Quick Summary

### What You Need:

1. **GitHub Account** - Your code must be on GitHub ✓ (you already have this!)
2. **Render.com Account** - Free hosting platform (sign up with GitHub)
3. **Custom Domain** - Purchase from Namecheap, Google Domains, etc. (~$10-20/year)
4. **Gmail App Password** - For equacare77@gmail.com contact form

### Total Time: 
- **Deployment:** 30-60 minutes (mostly waiting for DNS)
- **Content Setup:** 1-2 hours (adding content via admin)

### Total Cost:
- **Domain:** $10-20/year
- **Hosting:** FREE (Render.com free tier)
- **SSL Certificate:** FREE (auto-provided)
- **Total:** ~$10-20/year

---

## 🚀 Quick Start (3 Steps)

### Step 1: Deploy to Render (15 minutes)

1. Go to https://render.com
2. Sign in with GitHub
3. Create "Web Service" from your repository
4. Configure:
   - Build: `./build.sh`
   - Start: `gunicorn equacare_project.wsgi:application`
   - Add environment variables (see guide)
5. Deploy!

**You'll get:** `https://equacare.onrender.com`

---

### Step 2: Get a Domain (5 minutes + payment)

1. Go to https://www.namecheap.com (or Google Domains)
2. Search for your domain (e.g., "equacare.com")
3. Purchase for ~$10-20/year
4. Complete checkout

**You'll have:** `equacare.com` (or your chosen domain)

---

### Step 3: Connect Domain (15-30 minutes + DNS wait)

1. In Render: Add custom domain
2. In Domain Registrar: Add DNS records
3. Wait for DNS propagation (15 min - 24 hours)
4. Verify and get free SSL

**You'll have:** `https://www.equacare.com` with SSL!

---

## 🎉 After Deployment

Once live, you'll need to:

1. **Create Admin User**
   ```bash
   python manage.py createsuperuser
   ```

2. **Add Content** via Admin Panel
   - Go to: `https://yourdomain.com/admin/`
   - Add: Site Settings, Services, Hero Section, etc.

3. **Test Everything**
   - All pages load correctly
   - Contact form works
   - Images display properly
   - Mobile-responsive

---

## 🆘 Need Help?

### Common Issues:

**"Domain not working"**
→ DNS takes time to propagate (wait 1-24 hours)
→ Check DNS records at https://dnschecker.org

**"400 Bad Request"**
→ Add domain to ALLOWED_HOSTS in settings.py
→ See CUSTOM_DOMAIN_GUIDE.md

**"SSL not working"**
→ Wait 15-30 minutes after domain verification
→ Render auto-provisions SSL

### Support Resources:

- **Render Docs:** https://render.com/docs
- **Django Docs:** https://docs.djangoproject.com/en/4.2/howto/deployment/
- **DNS Checker:** https://dnschecker.org

---

## ✅ Pre-Deployment Checklist

Before you start, make sure you have:

- [x] Code pushed to GitHub ✓
- [ ] Render.com account (will create)
- [ ] Domain purchased (will purchase)
- [ ] Gmail App Password for equacare77@gmail.com
- [ ] Generated SECRET_KEY for production

**Generate SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

---

## 📊 What's Already Configured

Your project is already deployment-ready! ✅

**Files configured:**
- ✅ `settings.py` - Production settings with custom domain support
- ✅ `build.sh` - Build script for Render
- ✅ `requirements.txt` - All dependencies listed
- ✅ `Procfile` - Process configuration
- ✅ `render.yaml` - Render configuration
- ✅ WhiteNoise - Static files handling
- ✅ Gunicorn - WSGI server
- ✅ PostgreSQL support - Database ready

**What you updated:**
- ✅ Enhanced ALLOWED_HOSTS for custom domains
- ✅ Added CUSTOM_DOMAIN environment variable support
- ✅ CSRF trusted origins for custom domains

**You just need to:**
1. Deploy it
2. Get a domain
3. Connect them

---

## 🎯 Deployment Options Comparison

### Option 1: Render.com (Recommended) ⭐

**Pros:**
- ✅ Completely FREE
- ✅ Easy setup (5 minutes)
- ✅ Auto-deploy from GitHub
- ✅ Free PostgreSQL database
- ✅ Free SSL certificate
- ✅ Custom domain support

**Cons:**
- ⚠️ Sleeps after 15 min inactivity
- ⚠️ Takes ~30 sec to wake up

**Best for:** Most users, free hosting

---

### Option 2: Railway.app

**Pros:**
- ✅ Fast deployment
- ✅ Good free tier
- ✅ Auto-deploy from GitHub

**Cons:**
- ⚠️ Free tier has usage limits
- ⚠️ May require credit card

**Best for:** Alternative to Render

---

### Option 3: DigitalOcean App Platform

**Pros:**
- ✅ No sleep mode
- ✅ Better performance
- ✅ Predictable pricing

**Cons:**
- ❌ Costs $5/month minimum
- ⚠️ More complex setup

**Best for:** Production sites with traffic

---

## 💡 Pro Tips

1. **Use Render's free tier first** - Test everything before considering paid hosting
2. **Keep credentials secure** - Never commit secrets to Git
3. **Use environment variables** - For all sensitive data
4. **Set up UptimeRobot** - Keeps your Render site awake (free)
5. **Enable auto-deploy** - Render deploys automatically on Git push
6. **Backup your database** - Download backups monthly
7. **Monitor your site** - Check Google Analytics and uptime

---

## 🎓 Learning Resources

**New to deployment?** Check these out:

- **Render Docs:** https://render.com/docs/web-services
- **Django Deployment:** https://docs.djangoproject.com/en/4.2/howto/deployment/
- **DNS Basics:** https://www.cloudflare.com/learning/dns/what-is-dns/
- **SSL/HTTPS:** https://letsencrypt.org/getting-started/

---

## 📞 Support

**Technical Issues:**
- Check `CUSTOM_DOMAIN_GUIDE.md` troubleshooting section
- Render Support: https://community.render.com
- Django Forums: https://forum.djangoproject.com

**Domain/DNS Issues:**
- Your registrar's support (Namecheap, GoDaddy, etc.)
- DNS Propagation Checker: https://dnschecker.org

---

## 🎉 Ready to Deploy?

### Next Steps:

1. **Open:** `DEPLOY_CUSTOM_DOMAIN.md`
2. **Print:** `DEPLOYMENT_CHECKLIST.md`
3. **Start:** Deploying your site!

**Time to go live! 🚀**

---

## 📝 Quick Reference Commands

### Check if code is pushed to GitHub:
```bash
git status
git remote -v
```

### Generate SECRET_KEY:
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

### Test locally before deploying:
```bash
python manage.py runserver
# Visit: http://127.0.0.1:8000
```

### Create superuser (after deployment):
```bash
# In Render Shell:
python manage.py createsuperuser
```

---

**Good luck with your deployment!** 🎉

Your professional website will be live soon! 🌟

---

*Questions? Refer to the detailed guides or reach out to your developer.*

