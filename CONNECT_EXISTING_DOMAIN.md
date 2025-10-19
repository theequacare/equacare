# ⚡ Connect Your Existing Domain to Render

**Your Live Site:** https://equacare-91mc.onrender.com/  
**What You Have:** ✅ Domain already purchased  
**What You Need:** Connect it to Render

**Time Required:** 10 minutes active work + DNS wait time  
**Cost:** $0 (you already own the domain!)

---

## 🚀 Quick 3-Step Process

```
Step 1: Add domain in Render (2 min)
   ↓
Step 2: Update DNS records (5 min)
   ↓
Step 3: Add environment variable (2 min)
   ↓
DONE! ✅
```

---

## STEP 1: Add Your Domain to Render (2 minutes)

### 1.1 Go to Render Dashboard
- Visit: https://dashboard.render.com
- Click on: **`equacare-91mc`** (your web service)

### 1.2 Add Custom Domain
- Click: **"Settings"** tab
- Scroll down to: **"Custom Domain"** section
- Click: **"Add Custom Domain"**

### 1.3 Add Both Versions
**First, add the www version:**
```
www.yourdomain.com
```
Click **"Save"**

**Then, add the root domain:**
```
yourdomain.com
```
Click **"Save"**

*Replace `yourdomain.com` with your actual domain*

### 1.4 Note the DNS Instructions
Render will show you the DNS records you need. **Copy these down** or keep the page open!

---

## STEP 2: Update DNS at Your Domain Registrar (5 minutes)

You need to add DNS records at whichever company you bought your domain from (Namecheap, GoDaddy, Google Domains, Cloudflare, etc.).

### The DNS Records You Need:

**Record 1 (for www):**
```
Type: CNAME
Name/Host: www
Value/Target: equacare-91mc.onrender.com
TTL: Automatic or 3600
```

**Record 2 (for root domain):**
```
Type: CNAME
Name/Host: @
Value/Target: equacare-91mc.onrender.com
TTL: Automatic or 3600
```

### Instructions by Registrar:

<details>
<summary><b>📘 Namecheap</b></summary>

1. Log into: https://www.namecheap.com
2. Go to: **Domain List**
3. Click: **"Manage"** next to your domain
4. Click: **"Advanced DNS"** tab
5. Delete any existing CNAME or A records for `@` and `www`
6. Click: **"Add New Record"**
7. Add the two records above
8. Click: **"Save All Changes"**

</details>

<details>
<summary><b>🌐 GoDaddy</b></summary>

1. Log into: https://www.godaddy.com
2. Go to: **My Products** → **Domains**
3. Click: **DNS** next to your domain
4. Scroll to: **Records** section
5. Delete any existing CNAME or A records for `@` and `www`
6. Click: **"Add"** button
7. Add the two records above
8. Click: **"Save"**

</details>

<details>
<summary><b>🔷 Google Domains</b></summary>

1. Log into: https://domains.google.com
2. Click on your domain
3. Click: **DNS** in the left menu
4. Scroll to: **Custom records**
5. Delete any existing records for `@` and `www`
6. Click: **"Create new record"**
7. Add the two records above
8. Click: **"Save"**

</details>

<details>
<summary><b>☁️ Cloudflare</b></summary>

1. Log into: https://dash.cloudflare.com
2. Select your domain
3. Go to: **DNS** → **Records**
4. Delete any existing CNAME or A records for `@` and `www`
5. Click: **"Add record"**
6. Add the two records above
7. **Important:** Set Proxy status to **"Proxied"** (orange cloud)
8. Click: **"Save"**

</details>

<details>
<summary><b>📦 Other Registrars</b></summary>

The process is similar for all registrars:
1. Find **DNS Settings** or **DNS Management**
2. Look for **CNAME Records** or **DNS Records**
3. Add the two records above
4. Save changes

</details>

---

## STEP 3: Add Environment Variable in Render (2 minutes)

### 3.1 Go to Environment Tab
- In Render Dashboard, click on your `equacare-91mc` service
- Click: **"Environment"** tab

### 3.2 Add Custom Domain Variable
- Click: **"Add Environment Variable"**
- Enter:
  ```
  Key: CUSTOM_DOMAIN
  Value: yourdomain.com,www.yourdomain.com
  ```
  *Replace with your actual domain*

### 3.3 Save and Redeploy
- Click: **"Save Changes"**
- Render will automatically redeploy (takes ~5 minutes)

---

## ⏰ Wait for DNS Propagation

DNS changes can take time to propagate:
- **Minimum:** 15 minutes
- **Typical:** 1-2 hours  
- **Maximum:** 24-48 hours

### Check if DNS is Ready:

1. Go to: **https://dnschecker.org**
2. Enter: `www.yourdomain.com`
3. Select: **CNAME**
4. Click: **Search**
5. Look for: `equacare-91mc.onrender.com` in results

When most locations show your Render URL → DNS is ready! ✅

---

## ✅ Verify Domain in Render

Once DNS is propagated:

1. Go back to Render Dashboard
2. Click on your `equacare-91mc` service
3. Go to: **Settings** → **Custom Domain**
4. Click: **"Verify"** next to your domain
5. If successful, you'll see a **green checkmark** ✅
6. Render will automatically provision **free SSL certificate** (takes 5-15 minutes)

---

## 🎉 Test Your Website!

Once SSL is active (green checkmark in Render), visit:

### Test Both URLs:
- ✅ **https://www.yourdomain.com**
- ✅ **https://yourdomain.com**

### Verify Everything Works:
- [ ] Homepage loads
- [ ] All pages work (About, Services, Knowledge, Careers, Contact)
- [ ] Images display correctly
- [ ] Contact form works
- [ ] Green padlock 🔒 (HTTPS/SSL working)
- [ ] Admin panel: **https://yourdomain.com/admin/**

---

## 📋 Quick Copy-Paste Reference

### For Render (Custom Domain):
```
www.yourdomain.com
yourdomain.com
```

### For Your DNS (replace `yourdomain.com`):
```
Type: CNAME | Host: www | Value: equacare-91mc.onrender.com
Type: CNAME | Host: @   | Value: equacare-91mc.onrender.com
```

### For Render (Environment Variable):
```
CUSTOM_DOMAIN = yourdomain.com,www.yourdomain.com
```

---

## 🐛 Troubleshooting

### Issue: "This site can't be reached"
**Cause:** DNS not propagated yet  
**Fix:** Wait longer and check https://dnschecker.org

---

### Issue: "400 Bad Request" or "Invalid Host"
**Cause:** CUSTOM_DOMAIN environment variable not set  
**Fix:** 
1. Add CUSTOM_DOMAIN env var in Render
2. Wait for redeploy to complete (~5 min)

---

### Issue: "Your connection is not private" (SSL error)
**Cause:** SSL certificate still provisioning  
**Fix:** Wait 15-30 minutes after domain verification

---

### Issue: Only www works (or vice versa)
**Cause:** Missing one of the domains or DNS records  
**Fix:** 
1. Verify BOTH domains added in Render
2. Verify BOTH DNS records created
3. Wait for DNS propagation

---

### Issue: CNAME for @ not allowed
**Cause:** Some registrars don't allow CNAME for root domain  
**Fix:** Use one of these alternatives:
- **Option A:** ALIAS record (if available) pointing to `equacare-91mc.onrender.com`
- **Option B:** A record pointing to Render's IP (check Render dashboard)
- **Option C:** URL redirect from @ to www

---

## 💡 Pro Tips

1. **Set DNS TTL to 300 (5 minutes)** initially - makes changes faster
2. **After everything works,** increase TTL to 3600 (1 hour) for better performance
3. **Clear your browser cache** if you see old content
4. **Use incognito/private mode** for testing to avoid cache issues
5. **Check https://status.render.com** if having issues

---

## 🎯 After Going Live

### Update Your Business:
- [ ] Update business cards
- [ ] Update email signature  
- [ ] Update social media links
- [ ] Update Google Business Profile
- [ ] Update any printed materials

### SEO Setup:
- [ ] Submit to Google Search Console: https://search.google.com/search-console
- [ ] Submit sitemap: `https://yourdomain.com/sitemap.xml`
- [ ] Set up Google Analytics (optional)

### Keep Site Awake (Optional):
- [ ] Sign up at: https://uptimerobot.com (FREE)
- [ ] Add monitor for your domain
- [ ] Set check interval to 5 minutes
- [ ] Keeps your Render site awake 24/7

---

## 📞 Support

**Check DNS Propagation:**
- https://dnschecker.org
- https://www.whatsmydns.net

**Render Support:**
- Dashboard: https://dashboard.render.com
- Docs: https://render.com/docs/custom-domains
- Community: https://community.render.com
- Status: https://status.render.com

**Your Domain Registrar:**
- Find their support/help center
- Usually have live chat or phone support

---

## ✅ Complete Checklist

- [ ] Added www.yourdomain.com in Render
- [ ] Added yourdomain.com in Render
- [ ] Added CNAME record for www
- [ ] Added CNAME record for @
- [ ] Saved DNS changes
- [ ] Added CUSTOM_DOMAIN environment variable in Render
- [ ] Waited for Render redeploy
- [ ] Waited for DNS propagation (checked at dnschecker.org)
- [ ] Verified domains in Render
- [ ] SSL certificate active (green checkmark)
- [ ] Tested https://www.yourdomain.com ✅
- [ ] Tested https://yourdomain.com ✅
- [ ] All pages working ✅
- [ ] Contact form tested ✅
- [ ] Admin panel accessible ✅

---

## 🎉 You're Done!

Once all steps are complete, your website will be live at:

**https://www.yourdomain.com**

With:
- ✅ Your custom domain
- ✅ Free SSL/HTTPS (green padlock)
- ✅ Professional branding
- ✅ Auto-deploy from GitHub
- ✅ Free hosting

**Congratulations! 🎊**

---

## 📞 Need Help?

**What's your domain name?** Let your developer know so they can help troubleshoot if needed.

**Stuck on a step?** Check the other detailed guides in your project folder or reach out to Render support.

---

**Ready? Let's connect your domain! 🚀**

Start with **STEP 1** above!

