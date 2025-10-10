# Email Notification Setup Guide

All contact form submissions and job applications will now be sent to: **equacare77@gmail.com**

## 📧 Gmail App Password Setup

To allow Django to send emails through Gmail, you need to create an **App Password**:

### Step 1: Enable 2-Factor Authentication

1. Go to your Google Account: https://myaccount.google.com/
2. Click **Security** in the left sidebar
3. Under "Signing in to Google", click **2-Step Verification**
4. Follow the prompts to enable 2-Step Verification if not already enabled

### Step 2: Create App Password

1. Go to: https://myaccount.google.com/apppasswords
2. Sign in to your Google Account (equacare77@gmail.com)
3. Under "Select app", choose **Mail**
4. Under "Select device", choose **Other (Custom name)**
5. Type: **Equacare Django Website**
6. Click **Generate**
7. Google will display a 16-character password (e.g., `abcd efgh ijkl mnop`)
8. **Copy this password** - you'll need it in the next step

### Step 3: Set Environment Variable

#### For Local Development (Mac/Linux):

```bash
export EMAIL_PASSWORD="your-16-character-app-password-here"
```

Add this to your `~/.zshrc` or `~/.bash_profile` to make it permanent:

```bash
echo 'export EMAIL_PASSWORD="your-16-character-app-password-here"' >> ~/.zshrc
source ~/.zshrc
```

#### For Production (Railway):

1. Go to your Railway dashboard
2. Click on your project
3. Go to **Variables** tab
4. Click **New Variable**
5. Add:
   - **Variable**: `EMAIL_PASSWORD`
   - **Value**: Your 16-character app password (no spaces)
6. Click **Add**
7. Redeploy your application

### Step 4: Test Email Configuration

After setting the environment variable, restart your Django server:

```bash
cd /Users/equacare/Documents/equacare
source venv/bin/activate
python manage.py shell
```

Then test sending an email:

```python
from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Test Email from Equacare',
    'This is a test email to verify the configuration.',
    settings.DEFAULT_FROM_EMAIL,
    ['equacare77@gmail.com'],
    fail_silently=False,
)
```

If successful, you should receive an email at equacare77@gmail.com!

---

## 📬 What Gets Emailed

### Contact Form Submissions:
- **Subject**: New Contact Form Submission: [Subject]
- **Contains**:
  - Name, Email, Phone
  - Subject and Message
  - Timestamp

### Job Applications:
- **Subject**: New Job Application: [Position] - [Name]
- **Contains**:
  - Position applied for
  - Applicant information
  - Cover letter text
  - **Resume attached as PDF/DOC**
  - Link to view in admin panel

---

## 🔒 Security Notes

- ✅ App Password is different from your Gmail password
- ✅ App Password only works for this application
- ✅ You can revoke the App Password anytime
- ✅ Never commit the password to GitHub (it's stored as environment variable)

---

## ✅ Email Features Active

1. **Contact Form** (http://127.0.0.1:8000/contact/)
   - Every submission sends email notification
   
2. **Career Applications** (http://127.0.0.1:8000/careers/)
   - Every application sends email with resume attached
   
3. **Home Page Contact Form**
   - Every submission sends email notification

---

## 🚨 Troubleshooting

### "Connection refused" error:
- Make sure 2-Factor Authentication is enabled
- Verify you're using the App Password, not your regular password

### "Authentication failed" error:
- Double-check the App Password (16 characters, no spaces)
- Make sure EMAIL_PASSWORD environment variable is set

### Emails not being received:
- Check your Gmail spam folder
- Verify the App Password is still active in Google Account settings
- Make sure your Django server is running

### To check if environment variable is set:
```bash
echo $EMAIL_PASSWORD
```

---

## 📝 Current Configuration

```python
EMAIL: equacare77@gmail.com
SMTP HOST: smtp.gmail.com
PORT: 587
TLS: Enabled
```

All emails will appear to come from: **equacare77@gmail.com**

---

**Need help?** Contact your developer or check Django email documentation:
https://docs.djangoproject.com/en/4.2/topics/email/

