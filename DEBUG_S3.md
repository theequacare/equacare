# S3 Photo Upload Debugging Guide

## Issue: Photos not showing after upload to Render

### ✅ What to Check:

#### 1. **Verify Render Environment Variables**
Go to Render Dashboard → Your Service → Environment

**Make sure ALL these are set:**
```
USE_S3=True
AWS_STORAGE_BUCKET_NAME=equacare-website-files
AWS_S3_REGION_NAME=us-east-2
AWS_ACCESS_KEY_ID=(your access key)
AWS_SECRET_ACCESS_KEY=(your secret key)
```

**IMPORTANT**: After setting environment variables, Render will automatically redeploy!

#### 2. **Check Render Deployment Logs**
1. Go to Render Dashboard
2. Click on your service
3. Click "Logs" tab
4. Look for any errors related to:
   - `boto3`
   - `django-storages`
   - `S3`
   - `AWS`
   - Import errors

#### 3. **Check S3 Bucket**
1. Go to AWS S3 Console
2. Open bucket: `equacare-website-files`
3. Look for folder: `media/ceo/`
4. **If the photo is there**: The upload worked! The issue is with display.
5. **If the photo is NOT there**: The upload failed.

#### 4. **Test Photo Upload Again**
After Render redeploys:
1. Go to: https://equacare-91mc.onrender.com/admin/
2. Login: `admin` / `admin123`
3. Delete the old CEO section entry
4. Create a NEW CEO section
5. Fill in all details
6. Upload CEO photo
7. Save
8. Check: https://equacare-91mc.onrender.com/about/

#### 5. **Check Photo URL**
On the about page, right-click → "Inspect Element" on the CEO photo area.

**Expected URL format:**
```
https://equacare-website-files.s3.us-east-2.amazonaws.com/media/ceo/photo-name.jpg
```

**If URL is wrong**, it means settings are incorrect.

---

## 🔧 Quick Fix Steps:

### Step 1: Verify Environment Variables
**In Render Dashboard:**
- USE_S3 = `True` (not "true" or "TRUE")
- AWS_STORAGE_BUCKET_NAME = `equacare-website-files`
- AWS_S3_REGION_NAME = `us-east-2`
- AWS_ACCESS_KEY_ID = (your key)
- AWS_SECRET_ACCESS_KEY = (your secret)

### Step 2: Wait for Redeploy
Wait 2-3 minutes for Render to redeploy after changing environment variables.

### Step 3: Check Logs
Look for:
```
✅ Good: "Collecting static files..."
✅ Good: "Running migrations..."
❌ Bad: "ModuleNotFoundError: No module named 'custom_storages'"
❌ Bad: "botocore.exceptions.ClientError"
```

### Step 4: Re-upload Photo
Delete old CEO section, create new one with photo.

---

## 🚨 Common Issues:

### Issue 1: `ModuleNotFoundError: No module named 'custom_storages'`
**Fix**: The new code didn't deploy properly. Force redeploy:
- Go to Render → Manual Deploy → "Clear build cache & deploy"

### Issue 2: Photo uploads but doesn't display
**Fix**: Check S3 bucket permissions:
- Block Public Access: All should be OFF
- Bucket Policy: Should allow public read

### Issue 3: `AccessDenied` error
**Fix**: Check IAM user has the custom policy with full S3 access.

### Issue 4: URL shows `/media/media/ceo/photo.jpg` (double media)
**Fix**: Already fixed in custom_storages.py

---

## 📞 What to Tell Me:

Please check and tell me:
1. ✅ or ❌ All environment variables are set in Render
2. ✅ or ❌ Render deployment completed successfully
3. ✅ or ❌ Any errors in Render logs
4. ✅ or ❌ Photo appears in S3 bucket after upload
5. What URL appears when you inspect the photo element

