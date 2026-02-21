from django.db import models


class ContactMessage(models.Model):
    """
    Stores messages submitted from the Contact page.
    Visible in /admin/ for the store owner to review.
    """
    name    = models.CharField(max_length=100)
    email   = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
