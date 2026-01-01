
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
# Job Board

A simple Django-based job board application providing job listings, company profiles, user accounts for candidates and employers, and application management.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running Locally](#running-locally)
- [Testing](#testing)
- [Deployment Notes](#deployment-notes)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This repository implements a job board built with Django. It supports:
- Employer accounts to post and manage jobs and company profiles.
- Candidate accounts to browse jobs and submit applications.
- Application tracking and basic dashboards for each user type.

## Features

- Authentication (register / login / logout)
- Role-based dashboards (candidate / employer)
- CRUD for jobs and companies (employers)
- Job application submission and status management
- Template-based views for common pages

## Tech Stack

- Python 3.x
- Django (see `requirements.txt` for exact versions)
- SQLite (default development DB: `db.sqlite3`)

## Project Structure

Top-level folders and notable apps:
- `apps/accounts` — user models, auth forms, dashboards
- `apps/jobs` — job models, views, templates
- `apps/companies` — company profiles and forms
- `apps/applications` — application records and statuses
- `core` — project settings and URL configuration

## Requirements

Install dependencies from `requirements.txt` (created via `pip freeze` in this workspace).

## Installation

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply database migrations:

```bash
python manage.py migrate
```

4. Create a superuser (optional):

```bash
python manage.py createsuperuser
```

## Running Locally

Start the development server:

```bash
python manage.py runserver
```

Open your browser at `http://127.0.0.1:8000/`.

## Testing

Run the Django test suite:

```bash
python manage.py test
```

## Deployment Notes

- Replace SQLite with PostgreSQL (or another production-ready DB).
- Configure `DEBUG=False` and proper `ALLOWED_HOSTS` in `core/settings.py`.
- Serve static files via a CDN or `collectstatic` behind a web server.
- Use environment variables for secret keys and DB credentials.

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feat/my-change`.
3. Add tests and ensure existing tests pass.
4. Open a pull request describing your changes.

---

