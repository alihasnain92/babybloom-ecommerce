from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name', 'email', 'sent_at']
    search_fields = ['name', 'email', 'message']
    ordering      = ['-sent_at']
    readonly_fields = ['name', 'email', 'message', 'sent_at']  # Prevent accidental edits

    def has_add_permission(self, request):
        """Disable manual creation — messages come from the contact form only."""
        return False
