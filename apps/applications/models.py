# apps/applications/models.py
from django.db import models
from apps.accounts.models import User
from apps.jobs.models import Job


class Application(models.Model):
    candidate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "candidate"},
        related_name="applications",
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    resume = models.FileField(upload_to="resumes/")
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.username} → {self.job.title}"
