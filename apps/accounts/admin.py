# apps/accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Add 'role' to the existing fieldsets using tuple-unpacking
    fieldsets = (
        *BaseUserAdmin.fieldsets,
        ("Role", {"fields": ("role",)}),
    )

    # Ensure the 'role' field is available on the add form too
    add_fieldsets = (
        *BaseUserAdmin.add_fieldsets,
        ("Role", {"fields": ("role",)}),
    )

    list_display = ("username", "email", "role", "is_staff", "is_superuser")
    list_filter = ("role", "is_staff", "is_superuser")
    search_fields = ("username", "email")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "created_at", "updated_at")
    search_fields = ("user__username", "user__email")
