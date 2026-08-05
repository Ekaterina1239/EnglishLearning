from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "english_level", "is_staff", "is_moderator")
    list_filter = ("english_level", "is_staff", "is_moderator", "is_active")

    fieldsets = BaseUserAdmin.fieldsets + (
        ("English learning", {"fields": ("english_level", "is_moderator")}),
    )