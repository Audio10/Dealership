"""User models admin."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models 
from users.models import User

class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name', 'last_name')


admin.site.register(User, CustomUserAdmin)