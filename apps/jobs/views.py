# apps/jobs/views.py

from django.shortcuts import render, get_object_or_404
from .models import Job


def job_list_view(request):
    jobs = Job.objects.all().order_by("-posted_at")
    return render(request, "jobs/job_list.html", {"jobs": jobs})


def job_detail_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, "jobs/job_detail.html", {"job": job})
