# apps/jobs/models.py
from django.db import models
from apps.accounts.models import User
from apps.companies.models import Company


class Job(models.Model):
    employer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "employer"},
        related_name="jobs",
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} @ {self.company.name}"
