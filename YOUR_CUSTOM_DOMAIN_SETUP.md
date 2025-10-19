# 🎯 Connect YOUR Custom Domain - Step by Step

**Your Current Live Site:** https://equacare-91mc.onrender.com/  
**Status:** ✅ Working perfectly!

**Goal:** Get it at your own domain (like `www.equacare.com`)

---

## ⚡ What You Need to Do

Since your site is already live on Render, you just need:
1. **Buy a domain** (~5 minutes + $10-15)
2. **Connect it to Render** (~2 minutes)
3. **Update DNS** (~5 minutes + wait time)

**Total active work:** ~15 minutes  
**Total cost:** ~$10-15/year

---

## 🛒 STEP 1: Buy Your Domain (5 minutes)

### Recommended: Namecheap

1. **Go to:** https://www.namecheap.com
2. **Search for domain:** Try these options:
   - `equacare.com`
   - `equacareservices.com`
   - `equacarellc.com`
   - `equacare.care`
   - `equacare.health`

3. **Add to cart** (should be around $9-15/year)

4. **Create account using:**
   - Email: `equacare77@gmail.com`
   - Create strong password and **save it**

5. **Complete purchase**

6. **Important:** Save your login credentials somewhere safe!

---

## 🔗 STEP 2: Add Domain to Render (2 minutes)

1. **Go to:** https://dashboard.render.com

2. **Click on:** `equacare-91mc` (your web service)

3. **Click:** "Settings" tab at the top

4. **Scroll down to:** "Custom Domain" section

5. **Click:** "Add Custom Domain" button

6. **Add the WWW version first:**
   ```
   www.yourdomain.com
   ```
   *(Replace `yourdomain.com` with your actual domain)*
   
   Click **"Save"**

7. **Add the root domain:**
   ```
   yourdomain.com
   ```
   Click **"Save"**

8. **Copy the DNS information** Render shows you - you'll need it next!

---

## 🌐 STEP 3: Configure DNS at Namecheap (5 minutes)

1. **Log into:** https://www.namecheap.com

2. **Go to:** "Domain List" in your account

3. **Click:** "Manage" button next to your domain

4. **Click:** "Advanced DNS" tab

5. **Delete** any existing CNAME or A records for @ and www (if any)

6. **Click:** "Add New Record" and add these **TWO records:**

### Record 1 (WWW):
```
Type: CNAME Record
Host: www
Value: equacare-91mc.onrender.com
TTL: Automatic
```

### Record 2 (Root domain):
```
Type: CNAME Record
Host: @
Value: equacare-91mc.onrender.com
TTL: Automatic
```

**Note:** If Namecheap doesn't allow CNAME for `@`, use this instead:
```
Type: URL Redirect Record
Host: @
Value: https://www.yourdomain.com
TTL: Automatic
```

7. **Click:** "Save All Changes" (green checkmark button)

---

## ⏰ STEP 4: Wait for DNS Propagation (15 min - 2 hours)

DNS changes need time to spread across the internet.

### Check if it's ready:

1. **Go to:** https://dnschecker.org

2. **Enter:** `www.yourdomain.com`

3. **Select:** CNAME from dropdown

4. **Click:** Search

5. **Look for:** `equacare-91mc.onrender.com` in results

When **most locations** show `equacare-91mc.onrender.com` → DNS is ready! ✅

---

## ✅ STEP 5: Verify Domain in Render (1 minute)

1. **Go back to:** https://dashboard.render.com

2. **Click on:** Your `equacare-91mc` service

3. **Go to:** Settings → Custom Domain

4. **Click:** "Verify" button next to your domain

5. **If verified successfully:**
   - Render will show a green checkmark ✅
   - SSL certificate will be automatically provisioned (5-15 minutes)

---

## 🔐 STEP 6: Add Custom Domain to Django Settings (2 minutes)

1. **In Render Dashboard,** click on your service

2. **Go to:** "Environment" tab

3. **Click:** "Add Environment Variable"

4. **Add this:**
   ```
   Key: CUSTOM_DOMAIN
   Value: yourdomain.com,www.yourdomain.com
   ```
   *(Replace with your actual domain)*

5. **Click:** "Save Changes"

6. **Render will automatically redeploy** (takes ~5 minutes)

---

## 🎉 STEP 7: Test Your Website!

Once SSL certificate shows as active (green checkmark), visit:

### Test both versions:
- ✅ **https://www.yourdomain.com**
- ✅ **https://yourdomain.com**

### Check these:
- [ ] Homepage loads correctly
- [ ] All pages work (About, Services, Knowledge, Careers, Contact)
- [ ] Images display properly
- [ ] Contact form works
- [ ] Green padlock 🔒 shows (HTTPS/SSL working)
- [ ] Admin panel: https://yourdomain.com/admin/

---

## 📊 Quick Reference

### Your Information:
- **Current URL:** https://equacare-91mc.onrender.com/
- **Render App Name:** `equacare-91mc`
- **GitHub Repo:** https://github.com/theequacare/equacare
- **Render Dashboard:** https://dashboard.render.com

### DNS Records (your actual values):
```
Record 1:
Type: CNAME
Host: www
Value: equacare-91mc.onrender.com

Record 2:
Type: CNAME
Host: @
Value: equacare-91mc.onrender.com
```

### Environment Variable:
```
CUSTOM_DOMAIN = yourdomain.com,www.yourdomain.com
```

---

## 🐛 Troubleshooting

### "This site can't be reached"
**Reason:** DNS not propagated yet  
**Solution:** Wait longer, check https://dnschecker.org

### "400 Bad Request" or "Invalid Host"
**Reason:** CUSTOM_DOMAIN environment variable not set  
**Solution:** 
1. Add CUSTOM_DOMAIN env var in Render
2. Wait for redeploy to complete

### "Not Secure" / SSL Error
**Reason:** SSL certificate still provisioning  
**Solution:** Wait 15-30 minutes after domain verification

### Only www works (or vice versa)
**Reason:** Missing one of the domains  
**Solution:** 
1. Make sure BOTH domains added in Render (www and non-www)
2. Make sure BOTH DNS records created

---

## 💰 Cost Breakdown

| Item | Cost | Frequency |
|------|------|-----------|
| Domain (Namecheap) | $9-15 | Per year |
| Render Hosting | **FREE** | Forever |
| SSL Certificate | **FREE** | Auto-renews |
| **TOTAL** | **$9-15** | **Per year** |

**Set a reminder** to renew your domain before it expires!

---

## 🎯 After Going Live

### 1. Update Your Business Info:
- ✅ Update business cards with new domain
- ✅ Update email signature
- ✅ Update social media profiles
- ✅ Update Google Business Profile

### 2. Submit to Google (for SEO):
1. Go to: https://search.google.com/search-console
2. Add your domain
3. Verify ownership
4. Submit sitemap: `https://yourdomain.com/sitemap.xml`

### 3. Keep Site Awake (Optional - FREE):
If you want 24/7 availability without the 30-second wake time:

1. Go to: https://uptimerobot.com
2. Create free account
3. Add monitor for: `https://yourdomain.com`
4. Set check interval: 5 minutes
5. This pings your site every 5 minutes, keeping it awake

---

## 📞 Support Links

**Check DNS:**
- https://dnschecker.org
- https://www.whatsmydns.net

**Render Support:**
- Dashboard: https://dashboard.render.com
- Docs: https://render.com/docs/custom-domains
- Status: https://status.render.com

**Namecheap Support:**
- Help Center: https://www.namecheap.com/support/
- Live Chat: Available 24/7

---

## ✅ Complete Checklist

Print this and check off as you go:

- [ ] Domain purchased from registrar
- [ ] Saved domain login credentials
- [ ] Added www.yourdomain.com in Render
- [ ] Added yourdomain.com in Render
- [ ] Added CNAME record for www
- [ ] Added CNAME record for @
- [ ] Saved DNS changes
- [ ] Waited for DNS propagation
- [ ] Verified DNS at dnschecker.org
- [ ] Verified domain in Render
- [ ] Added CUSTOM_DOMAIN environment variable
- [ ] Waited for Render redeploy
- [ ] SSL certificate active (green checkmark)
- [ ] Tested https://www.yourdomain.com
- [ ] Tested https://yourdomain.com
- [ ] All pages working correctly
- [ ] Contact form tested
- [ ] Admin panel accessible
- [ ] Updated business materials
- [ ] Submitted to Google Search Console
- [ ] Set up UptimeRobot (optional)

---

## 🎉 Success!

Once all steps are complete, your professional website will be live at:

**https://www.yourdomain.com**

With:
- ✅ Custom branded domain
- ✅ Free SSL/HTTPS (green padlock)
- ✅ Professional appearance
- ✅ Auto-deploy from GitHub
- ✅ Free hosting forever

**Share it with the world! 🌟**

---

## 📝 Domain Name Suggestions

If your first choice is taken, here are alternatives:

**Business Name Variations:**
- equacare.com
- equacareservices.com
- equacarellc.com
- equacareinc.com
- theequacare.com
- myequacare.com

**Descriptive Domains:**
- equacarehomecare.com
- equacarehealthservices.com
- equacarehealth.com
- equacareathome.com

**Alternative TLDs:**
- equacare.care (very relevant!)
- equacare.health
- equacare.io
- equacare.us

Check availability at: https://www.namecheap.com

---

## 🚀 Ready to Start?

**Your action items right now:**

1. **First:** Go to https://www.namecheap.com and search for your domain
2. **Then:** Follow the steps above
3. **Timeline:** 30 minutes of work + DNS wait time
4. **Result:** Professional domain for your business! 🎉

---

**Questions? Check the other detailed guides in your project folder!**

**Good luck! You've got this! 💪**

