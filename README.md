
---
# Job Board Platform

A Django-based job board application designed to connect **employers**, **companies**, and **candidates**. The platform supports custom user roles, company profiles, job postings, and candidate applications with resume uploads.

---

## 🚀 Current Progress

### ✅ Accounts App
- Custom `User` model with `role` field (`employer`, `candidate`, `admin`).
- `Profile` model linked via `OneToOneField` to `User`.
- Signals (`post_save`) to auto-create and update `Profile` whenever a `User` is created or saved.
- Admin setup for managing `User` and `Profile`.

### ✅ Companies App
- `Company` model with fields for name, industry, and location.
- Admin registration for easy management.

### ✅ Jobs App
- `Job` model linked to `Company` and `User` (employer role).
- Fields for title, description, location, and posting date.
- Admin setup for job listings.

### ✅ Applications App
- `Application` model linked to `Job` and `User` (candidate role).
- Resume upload (`FileField` → stored in `media/resumes/`).
- Cover letter field.
- Admin setup for applications.

### ✅ Media Handling
- Configured `MEDIA_ROOT` and `MEDIA_URL`.
- Automatic directory creation for `resumes/` and `avatars/` upon first upload.
- Admin interface supports file uploads.

---

## 📅 Roadmap (Next 2 Weeks)

### Week 1
- [ ] Inline admin setup: edit `Profile` directly within `User` admin.
- [ ] Candidate avatar upload support (`media/avatars/`).
- [ ] Basic templates for job listings and applications.
- [ ] User registration and login views (with role assignment).

### Week 2
- [ ] Employer dashboard: create and manage jobs.
- [ ] Candidate dashboard: apply to jobs and track applications.
- [ ] Company dashboard: manage company details and associated jobs.
- [ ] File upload validation (resume formats: PDF/DOCX).
- [ ] Initial styling with Bootstrap/Tailwind.

---

## 🛠️ Tech Stack
- **Backend:** Django 5.x
- **Database:** PostgreSQL (configurable)
- **Frontend:** Django templates (to be extended with modern UI framework)
- **Storage:** Local `media/` directory for uploads (S3 support planned)

---

## ⚡ Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/job-board.git
   cd job-board
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the server:
   ```bash
   python manage.py runserver
   ```

6. Access the admin at:
   ```
   http://127.0.0.1:8000/admin
   ```

---

## 📂 Project Structure
```
apps/
  accounts/      # Custom User + Profile
  companies/     # Company model
  jobs/          # Job postings
  applications/  # Candidate applications
media/
  resumes/       # Uploaded resumes
  avatars/       # Candidate avatars (planned)
```

---
