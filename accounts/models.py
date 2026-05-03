from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    ROLE_USER = "user"
    ROLE_MODERATOR = "moderator"
    ROLE_ADMIN = "admin"
    ROLE_CHOICES = (
        (ROLE_USER, "Користувач"),
        (ROLE_MODERATOR, "Модератор"),
        (ROLE_ADMIN, "Адміністратор"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_USER)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"
