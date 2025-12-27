# apps/accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile


admin.site.site_header = "Job Board Administration"
admin.site.site_title = "Job Board Admin Portal"
admin.site.index_title = "Welcome to the Job Board Admin"


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

    fieldsets = (
        *BaseUserAdmin.fieldsets,
        ("Role", {"fields": ("role",)}),
    )

    add_fieldsets = (
        *BaseUserAdmin.add_fieldsets,
        ("Role", {"fields": ("role",)}),
    )

    list_display = ("username", "email", "role", "is_staff", "is_superuser")
    list_filter = ("role", "is_staff", "is_superuser")
    search_fields = ("username", "email")
