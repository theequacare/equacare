# ✅ Equacare Deployment Checklist

Print this or keep it handy while deploying!

---

## 🎯 Phase 1: Pre-Deployment

- [ ] Code is pushed to GitHub
- [ ] Gmail App Password created for equacare77@gmail.com
- [ ] Generated SECRET_KEY for production
  ```bash
  python -c "import secrets; print(secrets.token_urlsafe(50))"
  ```
- [ ] Decided on domain name (e.g., equacare.com)

---

## 🚀 Phase 2: Deploy to Render

- [ ] Created Render.com account (sign in with GitHub)
- [ ] Created new Web Service
- [ ] Connected GitHub repository
- [ ] Configured service settings:
  - [ ] Build Command: `./build.sh`
  - [ ] Start Command: `gunicorn equacare_project.wsgi:application`
  - [ ] Instance Type: Free
- [ ] Added environment variables:
  - [ ] `PYTHON_VERSION = 3.9.18`
  - [ ] `DEBUG = False`
  - [ ] `SECRET_KEY = [your generated key]`
  - [ ] `EMAIL_PASSWORD = [Gmail App Password]`
- [ ] Created PostgreSQL database (optional)
- [ ] Deployment successful - got Render URL
- [ ] Tested Render URL (e.g., https://equacare.onrender.com)

---

## 🌐 Phase 3: Custom Domain Setup

- [ ] Purchased domain from registrar
  - Registrar: _______________
  - Domain: _______________
  - Cost: _______________
  
- [ ] Added custom domain in Render:
  - [ ] Settings → Custom Domain
  - [ ] Added: www.yourdomain.com
  
- [ ] Configured DNS records at registrar:
  - [ ] Type: CNAME, Name: www, Value: equacare.onrender.com
  - [ ] Type: CNAME/A, Name: @, Value: [Render's value]
  
- [ ] Added CUSTOM_DOMAIN environment variable in Render:
  - [ ] `CUSTOM_DOMAIN = yourdomain.com,www.yourdomain.com`
  
- [ ] Waited for DNS propagation (checked at dnschecker.org)
- [ ] Verified domain in Render
- [ ] SSL certificate auto-provisioned (HTTPS working)

---

## ⚙️ Phase 4: Post-Deployment Configuration

- [ ] Created superuser via Render Shell:
  ```bash
  python manage.py createsuperuser
  ```
  - Username: _______________
  - Email: equacare77@gmail.com
  - Password: (keep secure!)

- [ ] Logged into admin panel: https://yourdomain.com/admin/
- [ ] Added content in Django Admin:
  - [ ] Site Settings (contact info, company details)
  - [ ] Hero Section (homepage hero image and text)
  - [ ] About Preview (homepage about section)
  - [ ] Services (at least 3-5 services)
  - [ ] Job Listings (if hiring)
  - [ ] Uploaded images
  - [ ] Uploaded documents (referral forms, etc.)

---

## 🧪 Phase 5: Testing

- [ ] Visited homepage: https://yourdomain.com
- [ ] Checked all pages:
  - [ ] Home
  - [ ] About
  - [ ] Services
  - [ ] Careers
  - [ ] Contact
  - [ ] Knowledge
- [ ] Tested contact form
- [ ] Verified email notification received
- [ ] Tested on mobile devices
- [ ] Checked all images load correctly
- [ ] Verified all links work
- [ ] Tested admin panel functionality
- [ ] Confirmed HTTPS/SSL working (green padlock in browser)

---

## 🎉 Phase 6: Launch

- [ ] Announced website launch
- [ ] Updated business cards with website URL
- [ ] Added website to Google Business Profile
- [ ] Submitted to Google Search Console
- [ ] Set up Google Analytics (optional)
- [ ] Configured email signature with website link
- [ ] Updated social media profiles with website
- [ ] Set up UptimeRobot to keep site awake (optional)

---

## 📊 Ongoing Maintenance

- [ ] Monitor uptime
- [ ] Check contact form submissions regularly
- [ ] Update job listings as needed
- [ ] Respond to inquiries promptly
- [ ] Backup database monthly
- [ ] Review and update content quarterly
- [ ] Check for Django security updates

---

## 📞 Support Contacts

**Hosting (Render):**
- Dashboard: https://dashboard.render.com
- Docs: https://render.com/docs
- Support: support@render.com

**Domain Registrar:**
- Company: _______________
- Login: _______________
- Support: _______________

**Developer:**
- Contact: _______________

---

## 🔐 Important Credentials (Store Securely!)

**Do NOT commit this information to Git!**

| Service | Username | Password/Key | Notes |
|---------|----------|--------------|-------|
| Render Account | ___________ | ___________ | |
| Django Admin | ___________ | ___________ | |
| Domain Registrar | ___________ | ___________ | |
| Database | ___________ | ___________ | Auto-generated |
| Gmail App Password | equacare77@gmail.com | ___________ | For contact form |

---

## 📝 Deployment Info

- **Deployment Date:** _______________
- **Domain:** _______________
- **Render URL:** _______________
- **Database Type:** PostgreSQL / SQLite
- **Hosting Plan:** Free / Paid
- **SSL Provider:** Let's Encrypt (via Render)
- **Python Version:** 3.9.18
- **Django Version:** 4.2.x

---

## 💰 Costs Breakdown

| Item | Cost | Frequency | Next Renewal |
|------|------|-----------|--------------|
| Domain Registration | $_____ | Yearly | __________ |
| Hosting (Render) | $0.00 | Free | N/A |
| SSL Certificate | $0.00 | Free | Auto-renew |
| **TOTAL** | **$_____** | **Per Year** | |

---

## 🎯 Success Metrics

After 1 month, check:
- [ ] Number of visitors: _______
- [ ] Contact form submissions: _______
- [ ] Job applications: _______
- [ ] Page views: _______
- [ ] Average session duration: _______

---

**✨ Deployment Complete! ✨**

**Live Website:** https://_______________

Share your achievement! 🎉

---

*Last Updated: _______________*
*Deployed By: _______________*

