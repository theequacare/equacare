# Creating Your Admin Account

## 🔐 How to Create Admin Login

You need to create a superuser account to access the Django admin panel.

### Step 1: Open Terminal

Navigate to your project folder and activate virtual environment:
```bash
cd /Users/equacare/Documents/equacare
source venv/bin/activate
```

### Step 2: Create Superuser

Run this command:
```bash
python manage.py createsuperuser
```

### Step 3: Follow the Prompts

You'll be asked for:

1. **Username**: (press Enter to use 'admin' or type your preferred username)
   ```
   Username: admin
   ```

2. **Email address**: 
   ```
   Email address: equacar77@gmail.com
   ```

3. **Password**: (type a password - it won't show while typing)
   ```
   Password: [your password here]
   ```

4. **Password confirmation**: (type the same password again)
   ```
   Password (again): [your password here]
   ```

### Step 4: Success!

You'll see:
```
Superuser created successfully.
```

### Step 5: Login

Now you can login at: http://127.0.0.1:8000/admin/

Use:
- **Username**: admin (or whatever you chose)
- **Password**: [the password you set]

---

## 💡 Password Tips

- Use a strong password
- Write it down somewhere safe
- You can create multiple admin accounts if needed

---

## 🔄 Forgot Password?

If you forget your password, you can reset it:
```bash
python manage.py changepassword admin
```

---

## 📝 Example

```bash
cd /Users/equacare/Documents/equacare
source venv/bin/activate
python manage.py createsuperuser

Username: admin
Email address: equacar77@gmail.com
Password: ********
Password (again): ********

Superuser created successfully.
```

Now go to: http://127.0.0.1:8000/admin/ and login!

