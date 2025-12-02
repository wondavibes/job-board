from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ("employer", "Employer"),
        ("candidate", "Candidate"),
        ("admin", "Admin"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # Email required and unique
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    # Optional extras
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    resume = models.FileField(
        upload_to="resumes/", blank=True, null=True
    )  # candidates only

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} – {self.user.get_role_display()}"  # type: ignore
