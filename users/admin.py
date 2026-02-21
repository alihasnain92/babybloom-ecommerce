from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Extends Django's built-in UserAdmin so all default fields
    (username, password change, permissions, groups) remain intact.
    We just add our custom fields on top.
    """
    model = CustomUser

    # Columns shown in the user list page
    list_display  = ['username', 'email', 'phone', 'is_staff', 'is_active', 'created_at']
    list_filter   = ['is_staff', 'is_active']
    search_fields = ['username', 'email', 'phone']
    ordering      = ['-created_at']

    # Add our custom fields to the edit form
    fieldsets = UserAdmin.fieldsets + (
        ('BabyBloom Extra', {
            'fields': ('phone', 'created_at'),
        }),
    )
    readonly_fields = ['created_at']

    # Add our custom fields to the add (create new user) form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('BabyBloom Extra', {
            'fields': ('email', 'phone'),
        }),
    )
