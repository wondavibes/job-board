from django.views.generic import CreateView, ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from .models import Application
from .forms import ApplicationForm
from apps.jobs.models import Job
from apps.accounts.mixins import CandidateRequiredMixin, EmployerRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class ApplyToJobView(LoginRequiredMixin, CandidateRequiredMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = "applications/apply.html"

    # STEP 1: Get the job the user wants to apply to
    # This runs BEFORE the form is displayed or processed
    def dispatch(self, request, *args, **kwargs):
        self.job = get_object_or_404(Job, id=kwargs["job_id"])
        return super().dispatch(request, *args, **kwargs)

    # STEP 2: Add job + candidate to the form BEFORE saving
    def form_valid(self, form):
        application = form.save(commit=False)
        application.job = self.job
        application.candidate = self.request.user
        application.save()
        return redirect("job_detail", job_id=self.job.pk)

    # STEP 3: Add job to the template context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job"] = self.job
        return context


class JobApplicantsView(EmployerRequiredMixin, ListView):
    model = Application
    template_name = "applications/job_applicants.html"
    context_object_name = "applications"

    def dispatch(self, request, *args, **kwargs):
        self.job = get_object_or_404(Job, id=kwargs.get("job_id"), employer=request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return (
            Application.objects.filter(job=self.job)
            .select_related("candidate")
            .order_by("-applied_at")
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["job"] = self.job
        return ctx

    def post(self, request, *args, **kwargs):
        application_id = request.POST.get("application_id")
        new_status = request.POST.get("status")

        # Use Application.Status.values directly (model defines Status)
        valid_statuses = Application.Status.values
        if application_id and new_status in valid_statuses:
            Application.objects.filter(id=application_id, job=self.job).update(status=new_status)

        return redirect("job_applicants", job_id=self.job.pk)

        
