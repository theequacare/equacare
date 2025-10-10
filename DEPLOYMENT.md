# Deployment Guide - Equacare LLC Website

## Push to GitHub

The repository has been initialized and all files have been committed. To push to GitHub, follow these steps:

### Option 1: Using HTTPS (Recommended)

1. **Create a GitHub repository** (if not already created)
   - Go to https://github.com/new
   - Repository name: `equacare`
   - Make it private or public as needed
   - **Do NOT** initialize with README, .gitignore, or license

2. **Set up GitHub authentication**
   
   For Personal Access Token (recommended):
   ```bash
   # Generate a personal access token at:
   # https://github.com/settings/tokens
   
   # Then push with:
   cd /Users/equacare/Documents/equacare
   git remote set-url origin https://YOUR_USERNAME@github.com/YOUR_USERNAME/equacare.git
   git push -u origin main
   # Enter your personal access token when prompted
   ```

### Option 2: Using SSH

1. **Set up SSH key** (if not already done)
   ```bash
   # Generate SSH key
   ssh-keygen -t ed25519 -C "your_email@example.com"
   
   # Add to SSH agent
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   
   # Copy public key
   cat ~/.ssh/id_ed25519.pub
   # Add this key to GitHub: https://github.com/settings/keys
   ```

2. **Change remote to SSH and push**
   ```bash
   cd /Users/equacare/Documents/equacare
   git remote set-url origin git@github.com:YOUR_USERNAME/equacare.git
   git push -u origin main
   ```

### Option 3: Using GitHub CLI (easiest)

1. **Install GitHub CLI**
   ```bash
   brew install gh  # On macOS
   ```

2. **Authenticate and push**
   ```bash
   cd /Users/equacare/Documents/equacare
   gh auth login
   gh repo create equacare --private --source=. --remote=origin --push
   ```

## After Pushing to GitHub

Once pushed, you can:

1. **Enable GitHub Pages** (for static hosting)
   - Go to repository Settings > Pages
   - Select branch: main
   - Note: This won't work for Django; use for documentation only

2. **Set up Continuous Deployment**
   - Connect to platforms like Heroku, Railway, or DigitalOcean
   - They can automatically deploy from your GitHub repository

## Production Deployment Options

### Option 1: Heroku

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: gunicorn equacare_project.wsgi
   ```
3. Deploy:
   ```bash
   heroku create equacare-app
   git push heroku main
   ```

### Option 2: Railway.app

1. Go to https://railway.app
2. Click "New Project" > "Deploy from GitHub"
3. Select your repository
4. Railway will auto-detect Django and deploy

### Option 3: DigitalOcean App Platform

1. Go to https://cloud.digitalocean.com/apps
2. Click "Create App" > "GitHub"
3. Select repository and branch
4. Configure build and run commands

### Option 4: PythonAnywhere

1. Go to https://www.pythonanywhere.com
2. Create account and web app
3. Clone your repository
4. Set up WSGI configuration

## Environment Variables for Production

Make sure to set these environment variables:

```
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=your-database-url (if using PostgreSQL)
EMAIL_HOST=your-smtp-host
EMAIL_PORT=587
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-password
```

## Pre-Deployment Checklist

- [ ] Create GitHub repository
- [ ] Push code to GitHub
- [ ] Set DEBUG=False for production
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up production database (PostgreSQL recommended)
- [ ] Configure static files serving
- [ ] Set up SSL/HTTPS
- [ ] Configure email backend
- [ ] Set up monitoring and logging
- [ ] Configure backup strategy

## Need Help?

For deployment assistance:
- Django Deployment: https://docs.djangoproject.com/en/4.2/howto/deployment/
- GitHub Docs: https://docs.github.com/
- Heroku Django: https://devcenter.heroku.com/articles/django-app-configuration

---

Good luck with your deployment! 🚀

