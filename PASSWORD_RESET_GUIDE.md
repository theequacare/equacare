# 🔐 Password Reset System - Complete Guide

Your Equacare website now has a complete password reset system for admin users!

---

## 🎯 Features Implemented

✅ **Forgot Password Form** - Users can request password reset  
✅ **Email Notifications** - Automatic email with reset link  
✅ **Secure Token System** - 24-hour expiring reset links  
✅ **Password Confirmation** - Double-check new password  
✅ **Beautiful UI** - Modern, professional design  
✅ **Admin Integration** - Link on admin login page  

---

## 📍 Password Reset URLs

### For Users:
- **Start Reset:** http://localhost:8001/admin/password_reset/
- **Admin Login:** http://localhost:8001/admin/ (has "Forgot Password?" link)

### System URLs (automatic):
- Reset form sent: `/admin/password_reset/done/`
- Confirm password: `/admin/reset/<uidb64>/<token>/`
- Reset complete: `/admin/reset/complete/`

---

## 🚀 How to Use (For Admin Users)

### Step 1: Request Password Reset

1. Go to: http://localhost:8001/admin/
2. Click **"🔒 Forgot your password?"** link
3. Enter your email address: `equacare77@gmail.com`
4. Click **"Send Reset Link"**

### Step 2: Check Email

1. Check inbox at `equacare77@gmail.com`
2. Look for email: **"Equacare Admin - Password Reset Request"**
3. Click the reset link in the email
   - ⏱️ Link expires in 24 hours

### Step 3: Set New Password

1. Enter your new password twice
2. Follow the password requirements:
   - At least 8 characters
   - Not too similar to username/email
   - Not entirely numeric
   - Not too common
3. Click **"Reset Password"**

### Step 4: Login

1. You'll see success message
2. Click **"Go to Login Page"**
3. Login with your new password!

---

## 📧 Email Configuration Required

For password reset emails to work, you need to configure email settings:

### Quick Setup:

```bash
# Add to ~/.zshrc
export EMAIL_PASSWORD="your-gmail-app-password"
```

Then restart Django server.

**See:** `EMAIL_SETUP.md` for complete email configuration instructions.

---

## 🧪 Testing Password Reset

### Test Without Email Setup:

If email is not configured, you can still test by checking console:

1. Request password reset
2. Check terminal where Django server is running
3. You'll see the reset link printed in console
4. Copy and paste the link in your browser

### Test With Email:

1. Configure email (see EMAIL_SETUP.md)
2. Request password reset with your email
3. Check inbox for reset email
4. Click link and reset password

---

## 🛠️ Technical Details

### Files Created:

```
templates/admin/
├── login.html                      # Added "Forgot Password?" link
├── password_reset_form.html        # Request reset form
├── password_reset_done.html        # Confirmation page
├── password_reset_email.html       # Email template
├── password_reset_subject.txt      # Email subject
├── password_reset_confirm.html     # Set new password form
└── password_reset_complete.html    # Success page
```

### URLs Added:

```python
/admin/password_reset/              # Request reset
/admin/password_reset/done/         # Email sent confirmation
/admin/reset/<uidb64>/<token>/     # Reset form (from email)
/admin/reset/complete/              # Success page
```

### Security Features:

- ✅ Tokens expire in 24 hours
- ✅ One-time use tokens
- ✅ Secure password hashing
- ✅ Email verification required
- ✅ Password strength validation
- ✅ CSRF protection on all forms

---

## 🎨 UI Features

- **Modern Design** - Beautiful gradient backgrounds
- **Responsive** - Works on all devices
- **User-Friendly** - Clear instructions
- **Professional** - Matches admin panel style
- **Animations** - Smooth hover effects
- **Error Handling** - Clear error messages

---

## 🔍 Troubleshooting

### Link says "Invalid or Expired"

**Cause:** Link used before or expired (24 hours)  
**Solution:** Request a new password reset

### Email not received

**Cause:** Email not configured or wrong email  
**Solution:**
1. Check EMAIL_PASSWORD is set
2. Verify email address is correct
3. Check spam folder
4. See EMAIL_SETUP.md for configuration

### Can't access /admin/password_reset/

**Cause:** Server not running or wrong URL  
**Solution:**
1. Ensure server is running on port 8001
2. Use full URL: http://localhost:8001/admin/password_reset/

### Password doesn't meet requirements

**Cause:** Password too weak  
**Solution:** Use a stronger password:
- At least 8 characters
- Mix of letters and numbers
- Not too common (like "password123")

---

## 📝 Admin Tasks

### View Password Reset Requests:

While password reset attempts aren't logged by default, you can:

1. Check email inbox for reset requests
2. Monitor Django logs
3. Check server console output

### Change Password Manually:

```bash
cd /Users/equacare/equacare
python3 manage.py changepassword admin
```

---

## 🔒 Security Best Practices

1. **Use Strong Passwords**
   - At least 12 characters
   - Mix of uppercase, lowercase, numbers, symbols

2. **Keep Email Secure**
   - Enable 2-Factor Authentication on email
   - Don't share email credentials

3. **Monitor Reset Requests**
   - Unexpected resets might indicate attack
   - Change password immediately if suspicious

4. **Update Regularly**
   - Change admin password every 90 days
   - Update Django and dependencies

---

## ✅ Testing Checklist

Test your password reset system:

- [ ] Visit `/admin/password_reset/`
- [ ] Enter email and submit
- [ ] Receive email (or see link in console)
- [ ] Click reset link
- [ ] Enter new password twice
- [ ] See success message
- [ ] Login with new password
- [ ] Test "Forgot Password?" link on login page
- [ ] Test with invalid/expired link
- [ ] Test with wrong email

---

## 🎓 For Developers

### Customize Email Template:

Edit: `templates/admin/password_reset_email.html`

### Change Email Subject:

Edit: `templates/admin/password_reset_subject.txt`

### Modify Token Expiry:

In `settings.py`:
```python
PASSWORD_RESET_TIMEOUT = 86400  # 24 hours in seconds
```

### Custom Styling:

Edit the `<style>` blocks in each template file.

---

## 📞 Need Help?

If you encounter issues:

1. Check Django console for errors
2. Verify email configuration
3. Test with simple password first
4. Check EMAIL_SETUP.md for email config
5. Ensure server is running

---

**Your password reset system is ready to use!** 🎉

Try it now: http://localhost:8001/admin/password_reset/

