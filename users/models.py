from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Extended user model for BabyBloom.
    Adds phone number and timestamps to Django's built-in AbstractUser.
    email is made unique so users can log in with email.
    is_staff is inherited from AbstractUser (grants /admin/ access).
    """
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
