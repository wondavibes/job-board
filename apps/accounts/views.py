from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import User
from typing import Optional
from apps.jobs.models import Job
from apps.applications.models import Application
from .decorators import employer_required, candidate_required

User = get_user_model()


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user: User = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # ROLE-BASED REDIRECTS
            if user.role == "candidate":
                return redirect("candidate_dashboard")
            elif user.role == "employer":
                return redirect("employer_dashboard")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
@candidate_required
def candidate_dashboard(request):
    # show only applications made by this candidate
    applications = Application.objects.filter(candidate=request.user)
    return render(
        request, "accounts/candidate_dashboard.html", {"applications": applications}
    )


@login_required
@employer_required
def employer_dashboard(request):
    # show only jobs posted by this employer
    jobs = Job.objects.filter(employer=request.user)
    return render(request, "accounts/employer_dashboard.html", {"jobs": jobs})


@login_required
@employer_required
def job_applicants_view(request, job_id: int):
    job = get_object_or_404(Job, id=job_id, employer=request.user)
    applications = Application.objects.filter(job=job)

    # Handle application status updates
    if request.method == "POST":
        application_id = request.POST.get("application_id")
        new_status = request.POST.get("status")
        if application_id and new_status in ["pending", "accepted", "rejected"]:
            app = get_object_or_404(Application, id=application_id, job=job)
            app.status = new_status
            app.save()

    return render(
        request,
        "accounts/job_applicants.html",
        {"job": job, "applications": applications},
    )
