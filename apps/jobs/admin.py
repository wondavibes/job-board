from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "employer", "location", "posted_at")
    list_filter = ("company", "location")
    search_fields = ("title", "company__name", "employer__username")
