# 🚀 Connect Custom Domain to Your Existing Render Deployment

**Your Status:** ✅ Already on GitHub | ✅ Already on Render

**What You Need:** Just connect a custom domain!

---

## 🎯 Quick Overview

Since you're already deployed, you only need to:
1. **Purchase a domain** (~$10-20/year) - if you don't have one
2. **Connect it to Render** (15 minutes)
3. **Configure DNS** (15 min to 24 hours)

**Total Time:** ~30 minutes active work + DNS wait time  
**Total Cost:** ~$10-20/year (just the domain!)

---

## Step 1: Get Your Current Render URL

1. Go to **https://dashboard.render.com**
2. Find your `equacare` web service
3. Note your current URL (something like `https://equacare.onrender.com` or `https://equacare-xxxx.onrender.com`)

**Write it down here:** _________________________________

---

## Step 2: Purchase a Domain (If You Don't Have One)

### Recommended Registrars:

**Option 1: Namecheap** (Most Popular)
- Website: https://www.namecheap.com
- Cost: ~$9-15/year
- Pros: Cheap, free WHOIS privacy, easy DNS
- Search for: `equacare.com`, `equacareservices.com`, `equacarellc.com`

**Option 2: Google Domains**
- Website: https://domains.google.com
- Cost: ~$12-20/year
- Pros: Simple, integrated with Google services

**Option 3: Cloudflare Registrar**
- Website: https://www.cloudflare.com/products/registrar/
- Cost: At-cost (usually cheapest)
- Pros: Best security, free CDN and DDoS protection

### Steps to Purchase:
1. Go to registrar website
2. Search for your desired domain
3. Add to cart
4. Create account (use: equacare77@gmail.com)
5. Complete purchase
6. **Save your login credentials!**

**Domain purchased:** _________________________________

---

## Step 3: Add Custom Domain in Render

1. Go to **https://dashboard.render.com**
2. Click on your **equacare** web service
3. Click the **"Settings"** tab (top menu)
4. Scroll down to **"Custom Domain"** section
5. Click **"Add Custom Domain"**
6. Enter your domain in **TWO parts**:

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

7. Render will show you DNS records to configure

**Screenshot or copy the DNS records shown!**

---

## Step 4: Configure DNS at Your Domain Registrar

Now you need to point your domain to Render. Instructions vary by registrar:

### For Namecheap:

1. Log into **https://www.namecheap.com**
2. Go to **"Domain List"**
3. Click **"Manage"** next to your domain
4. Click **"Advanced DNS"** tab
5. Click **"Add New Record"**

**Add these records:**

| Type | Host | Value | TTL |
|------|------|-------|-----|
| CNAME | www | `your-app.onrender.com` | Automatic |
| CNAME | @ | `your-app.onrender.com` | Automatic |

*Note: If CNAME for @ doesn't work, use:*
| Type | Host | Value | TTL |
|------|------|-------|-----|
| A | @ | [IP from Render] | Automatic |

6. Click **"Save All Changes"**

---

### For Google Domains:

1. Log into **https://domains.google.com**
2. Click on your domain
3. Click **"DNS"** in the left menu
4. Scroll to **"Custom records"**
5. Click **"Create new record"**

**Add these records:**

```
Host name: www
Type: CNAME
TTL: 3600
Data: your-app.onrender.com
```

```
Host name: @
Type: CNAME or A
TTL: 3600
Data: your-app.onrender.com (or IP from Render)
```

---

### For Cloudflare:

1. Log into **https://dash.cloudflare.com**
2. Select your domain
3. Go to **"DNS"** → **"Records"**
4. Click **"Add record"**

**Add these records:**

```
Type: CNAME
Name: www
Target: your-app.onrender.com
Proxy status: Proxied (orange cloud)
```

```
Type: CNAME
Name: @
Target: your-app.onrender.com
Proxy status: Proxied (orange cloud)
```

---

## Step 5: Wait for DNS Propagation

DNS changes can take time to propagate globally:
- **Minimum:** 15 minutes
- **Average:** 1-2 hours
- **Maximum:** 24-48 hours

### Check DNS Propagation:

Go to **https://dnschecker.org**
- Enter your domain
- Select "CNAME" type
- Click "Search"
- Wait until most locations show your Render URL

---

## Step 6: Verify Domain in Render

1. Go back to **Render Dashboard**
2. Go to your web service → **"Settings"** → **"Custom Domain"**
3. Next to your domain, click **"Verify"**
4. If DNS is propagated, it will verify successfully
5. Render will automatically provision a **free SSL certificate** (takes 5-15 minutes)

**Status indicators:**
- 🟡 Yellow: Pending verification
- 🟢 Green: Verified and SSL active
- 🔴 Red: Issue with DNS

---

## Step 7: Update Environment Variables in Render

1. In Render Dashboard, go to your web service
2. Click **"Environment"** tab
3. Click **"Add Environment Variable"**
4. Add:
   ```
   Key: CUSTOM_DOMAIN
   Value: yourdomain.com,www.yourdomain.com
   ```
5. Click **"Save Changes"**
6. Render will automatically redeploy (takes ~5 minutes)

---

## Step 8: Test Your Website!

Once SSL is active (green checkmark), visit:
- **https://www.yourdomain.com**
- **https://yourdomain.com**

Both should work and show your website with a padlock 🔒 (HTTPS)!

### Test Checklist:
- [ ] Homepage loads
- [ ] All pages work (About, Services, Contact, Careers, Knowledge)
- [ ] Images display correctly
- [ ] Contact form works
- [ ] Admin panel accessible at: https://yourdomain.com/admin/
- [ ] HTTPS working (green padlock)
- [ ] Both www and non-www versions work

---

## 🎉 Success!

Your website is now live at your custom domain!

**Share it:**
- Update business cards
- Add to email signature
- Update social media profiles
- Submit to Google Search Console

---

## 🐛 Troubleshooting

### "This site can't be reached"
**Solution:** DNS not propagated yet. Wait longer and check dnschecker.org

### "400 Bad Request" or "Invalid HTTP_HOST header"
**Solution:** 
1. Make sure CUSTOM_DOMAIN environment variable is set in Render
2. Wait for Render to redeploy after adding the variable

### "Your connection is not private" (SSL error)
**Solution:** 
1. SSL certificate is still provisioning. Wait 15-30 minutes after verification.
2. Try accessing via https:// (not http://)

### Domain shows "Not Found" on Render
**Solution:** DNS records might be wrong. Double-check:
- CNAME record for www points to your-app.onrender.com
- A or CNAME record for @ points to Render

### Only www version works (or vice versa)
**Solution:** 
- Make sure you added BOTH domains in Render (www and non-www)
- Make sure DNS has records for BOTH

---

## 📊 Quick Reference

### Your Information:
- **GitHub Repo:** https://github.com/theequacare/equacare
- **Render Dashboard:** https://dashboard.render.com
- **Current Render URL:** _________________________________
- **Custom Domain:** _________________________________
- **Domain Registrar:** _________________________________
- **Domain Purchase Date:** _________________________________
- **Domain Renewal Date:** _________________________________

### DNS Records (fill in your actual values):
```
Type: CNAME
Name: www
Value: _________________________________

Type: CNAME or A
Name: @
Value: _________________________________
```

### Important Links:
- **Check DNS:** https://dnschecker.org
- **Render Docs:** https://render.com/docs/custom-domains
- **Your Admin Panel:** https://yourdomain.com/admin/

---

## 💰 Costs

- **Domain:** $10-20/year (renews annually)
- **Render Hosting:** $0/year (FREE tier)
- **SSL Certificate:** $0/year (FREE, auto-renews)
- **Total:** ~$10-20/year

**Set a calendar reminder** to renew your domain before it expires!

---

## 🎯 Next Steps After Going Live

1. **Add to Google Search Console**
   - https://search.google.com/search-console
   - Submit sitemap
   - Monitor search presence

2. **Set up Google Analytics** (optional)
   - Track visitors
   - Understand user behavior

3. **Configure UptimeRobot** (optional, FREE)
   - https://uptimerobot.com
   - Keeps your Render site awake 24/7
   - Alerts you if site goes down

4. **Update Business Listings**
   - Google Business Profile
   - Social media links
   - Email signatures
   - Business cards

5. **Regular Maintenance**
   - Check contact form submissions weekly
   - Update job listings as needed
   - Monitor uptime
   - Backup database monthly

---

## 📞 Need Help?

**Render Support:**
- Docs: https://render.com/docs/custom-domains
- Community: https://community.render.com
- Status: https://status.render.com

**Domain Registrar Support:**
- Namecheap: https://www.namecheap.com/support/
- Google: https://support.google.com/domains/
- Cloudflare: https://support.cloudflare.com

**DNS Tools:**
- Propagation Checker: https://dnschecker.org
- DNS Lookup: https://mxtoolbox.com/DNSLookup.aspx
- What's My DNS: https://www.whatsmydns.net

---

**🎉 Congratulations! You're going live! 🎉**

**Follow these steps and your website will be at your own domain!**

---

*Questions? Check the other detailed guides in your project folder.*

