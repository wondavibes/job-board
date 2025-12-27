# apps/jobs/views.py

from django.shortcuts import render, get_object_or_404
from .models import Job

from django.views.generic import CreateView, UpdateView, DeleteView
from typing import cast
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from apps.accounts.mixins import EmployerRequiredMixin


def job_list_view(request):
    jobs = Job.objects.all().order_by("-posted_at")
    return render(request, "jobs/job_list.html", {"jobs": jobs})


def job_detail_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, "jobs/job_detail.html", {"job": job})


class JobCreateView(LoginRequiredMixin, EmployerRequiredMixin, CreateView):
    model = Job
    fields = ["title", "description", "location", "company"]  # adjust fields as needed
    template_name = "jobs/job_form.html"
    success_url = reverse_lazy("job_list")

    def form_valid(self, form):
        form.instance.employer = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "Create Job"
        return context


class JobUpdateView(LoginRequiredMixin, EmployerRequiredMixin, UpdateView):
    model = Job
    fields = ["title", "description", "location", "company"]  # adjust as needed
    template_name = "jobs/job_form.html"
    success_url = reverse_lazy("job_list")

    # STEP 1: Ensure only the employer who created the job can edit it
    def test_func(self):
        job = cast(Job, self.get_object())
        return job.employer == self.request.user

    # STEP 2: Optional — customize context if needed
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "Update Job"
        return context


class JobDeleteView(LoginRequiredMixin, EmployerRequiredMixin, DeleteView):
    model = Job
    template_name = "jobs/job_confirm_delete.html"
    success_url = reverse_lazy("job_list")

    def test_func(self):
        job = cast(Job, self.get_object())
        return job.employer == self.request.user
