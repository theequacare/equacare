# AWS S3 Setup Guide for Permanent File Storage

This guide will help you set up AWS S3 for permanent file storage, so your uploaded photos won't disappear.

## 🚀 Quick Setup (5 minutes)

### Step 1: Create AWS Account
1. Go to: https://aws.amazon.com/
2. Click "Create an AWS Account"
3. Follow the signup process (requires credit card, but S3 is very cheap)

### Step 2: Create S3 Bucket
1. **Go to AWS Console**: https://console.aws.amazon.com/
2. **Search for "S3"** in the search bar
3. **Click "Create bucket"**
4. **Bucket name**: `equacare-media-files` (must be globally unique)
5. **Region**: Choose closest to you (e.g., `us-east-1`)
6. **Uncheck "Block all public access"** (we need public access for images)
7. **Check "I acknowledge..."** warning
8. **Click "Create bucket"**

### Step 3: Create IAM User (for security)
1. **Go to IAM**: https://console.aws.amazon.com/iam/
2. **Click "Users"** → **"Create user"**
3. **Username**: `equacare-s3-user`
4. **Attach policies directly** → **"AmazonS3FullAccess"**
5. **Click "Next"** → **"Create user"**
6. **Click on the user** → **"Security credentials"** → **"Create access key"**
7. **Use case**: "Application running outside AWS"
8. **Click "Create access key"**
9. **SAVE THESE CREDENTIALS** (you'll need them):
   - Access Key ID
   - Secret Access Key

### Step 4: Configure Bucket Permissions
1. **Go back to S3** → **Your bucket** → **"Permissions"**
2. **Bucket Policy** → **Edit** → **Paste this policy**:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
        }
    ]
}
```

**Replace `YOUR-BUCKET-NAME` with your actual bucket name**

3. **Click "Save changes"**

## 🔧 Configure Render

### Step 1: Add Environment Variables to Render
1. **Go to Render Dashboard**: https://dashboard.render.com/
2. **Click your service** → **"Environment"**
3. **Add these environment variables**:

```
USE_S3=True
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
AWS_S3_REGION_NAME=us-east-1
```

### Step 2: Deploy
1. **Click "Manual Deploy"** on Render
2. **Wait for deployment to complete**

## ✅ Test It Works

1. **Go to your admin panel**: `https://your-site.onrender.com/admin/`
2. **Upload a new CEO photo**
3. **Check if it displays correctly**
4. **Photos will now be permanent!**

## 💰 Cost Estimate

- **S3 Storage**: ~$0.023 per GB per month
- **For 1GB of photos**: ~$0.023/month (less than 3 cents!)
- **Very affordable for small businesses**

## 🔒 Security Notes

- Your IAM user only has S3 access (not full AWS access)
- Files are publicly readable (needed for website images)
- You can always change permissions later

## 🆘 Need Help?

If you get stuck:
1. Check AWS documentation: https://docs.aws.amazon.com/s3/
2. Make sure bucket name is globally unique
3. Verify environment variables are set correctly in Render
4. Check Render deployment logs for errors

---

**Once set up, your photos will be permanent and accessible from anywhere!** 🎉
