from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .models import Application
from .forms import ApplicationForm
from apps.jobs.models import Job


class ApplyToJobView(CreateView):
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
