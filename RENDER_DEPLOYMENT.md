# 🚀 Deploying Equacare to Render.com (FREE)

This guide will help you deploy your Equacare website to Render.com for **completely free**.

---

## ✅ **Prerequisites**

- ✅ GitHub account (you already have this)
- ✅ Code pushed to GitHub (already done!)
- ✅ Email: equacare77@gmail.com

---

## 📋 **Step-by-Step Deployment**

### **Step 1: Create Render Account**

1. Go to **https://render.com**
2. Click **"Get Started"** (top right)
3. Sign up with **GitHub** (easiest option)
4. Authorize Render to access your GitHub repositories

---

### **Step 2: Create a New Web Service**

1. On your Render Dashboard, click **"New +"** button
2. Select **"Web Service"**
3. Connect your GitHub repository:
   - Find and select: **`tech-dipak/equacare`**
   - Click **"Connect"**

---

### **Step 3: Configure Your Service**

Fill in the following settings:

**Basic Settings:**
- **Name:** `equacare` (or any name you prefer)
- **Region:** Choose closest to Iowa (e.g., **Oregon (US West)**)
- **Branch:** `main`
- **Root Directory:** (leave blank)
- **Runtime:** `Python 3`
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn equacare_project.wsgi:application`

**Instance Type:**
- Select **"Free"** (this is important!)

---

### **Step 4: Add Environment Variables**

Click **"Advanced"** and add these environment variables:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.9.18` |
| `DEBUG` | `False` |
| `EMAIL_PASSWORD` | `[Your Gmail App Password]` |

**Important:** For `EMAIL_PASSWORD`, use the Gmail App Password you created earlier for `equacare77@gmail.com`.

> If you haven't created an App Password yet, follow the instructions in `EMAIL_SETUP.md`.

---

### **Step 5: Create PostgreSQL Database**

1. While still on the service configuration page, scroll down to **"Add Database"**
2. Click **"Create Database"**
3. Render will automatically:
   - Create a PostgreSQL database
   - Connect it to your web service
   - Set the `DATABASE_URL` environment variable

**Database Settings:**
- **Name:** `equacare_db`
- **Database:** `equacare_db`
- **User:** `equacare_user`
- **Region:** Same as your web service

---

### **Step 6: Deploy!**

1. Review all settings
2. Click **"Create Web Service"**
3. Render will now:
   - Install dependencies
   - Run migrations
   - Collect static files
   - Start your application

**This process takes 5-10 minutes.** ⏳

---

### **Step 7: Access Your Live Website**

Once deployment is complete, you'll see:
- ✅ **Green "Live"** status
- 🌐 Your website URL: `https://equacare.onrender.com` (or similar)

**Click the URL to visit your live website!** 🎉

---

## 🔧 **Post-Deployment Setup**

### **Create Admin User**

Your database is fresh, so you need to create an admin user:

1. On your Render dashboard, find your service
2. Click **"Shell"** tab
3. Run this command:
   ```bash
   python manage.py createsuperuser
   ```
4. Follow the prompts:
   - Username: `admin`
   - Email: `equacare77@gmail.com`
   - Password: (create a strong password)

### **Add Content via Admin**

1. Go to: `https://your-app.onrender.com/admin/`
2. Login with your superuser credentials
3. Add content:
   - **Site Settings** (contact info, company details)
   - **Hero Section** (homepage hero)
   - **About Preview** (homepage about section)
   - **Services**
   - **Job Listings**
   - Upload images and documents

---

## 📌 **Important Notes**

### **Free Tier Limitations:**

- ✅ **Free forever** (no credit card required)
- ✅ PostgreSQL database included
- ✅ SSL certificate (HTTPS)
- ✅ Custom domain support
- ⚠️ **Sleeps after 15 minutes of inactivity**
- ⚠️ Takes ~30 seconds to wake up on first visit

### **Wake-Up Solution:**

If the site sleeps and you want it to stay awake:
- Use a free service like **UptimeRobot** to ping your site every 5 minutes
- This keeps it active 24/7

---

## 🔄 **Auto-Deploy Updates**

**Good news!** Render automatically watches your GitHub repository.

**Whenever you push new code to GitHub:**
```bash
git add .
git commit -m "Update website"
git push origin main
```

**Render will automatically:**
1. Detect the changes
2. Rebuild your application
3. Deploy the updates

**No manual intervention needed!** 🎉

---

## 🎨 **Custom Domain (Optional)**

You can connect your own domain (e.g., `equacare.com`):

1. On Render dashboard, go to your service
2. Click **"Settings"** → **"Custom Domain"**
3. Add your domain
4. Update your domain's DNS records as instructed
5. Render provides free SSL certificate

---

## 🐛 **Troubleshooting**

### **Build Failed?**

Check the build logs:
- On Render dashboard, click on your service
- Go to **"Logs"** tab
- Look for error messages

Common issues:
- Missing dependencies (check `requirements.txt`)
- Syntax errors in code
- Database connection issues

### **Site Not Loading?**

1. Check the **"Logs"** tab for runtime errors
2. Verify environment variables are set correctly
3. Make sure `DEBUG=False` in production

### **Images Not Showing?**

1. Make sure you've uploaded images via admin panel
2. Check that `STATIC_ROOT` and `MEDIA_ROOT` are configured
3. Run `python manage.py collectstatic` manually in Shell if needed

---

## 📞 **Need Help?**

- **Render Docs:** https://render.com/docs
- **Render Community:** https://community.render.com
- **Django Deployment:** https://docs.djangoproject.com/en/4.2/howto/deployment/

---

## ✅ **Deployment Checklist**

- [ ] Render account created
- [ ] GitHub repository connected
- [ ] Web service configured
- [ ] PostgreSQL database created
- [ ] Environment variables set
- [ ] Deployment successful (green "Live" status)
- [ ] Website accessible at provided URL
- [ ] Admin user created
- [ ] Site Settings configured
- [ ] Content added via admin panel
- [ ] Test all pages and features
- [ ] Email notifications working

---

**🎉 Congratulations! Your Equacare website is now live!** 🎉

Visit your site and share the URL with the world! 🌍

