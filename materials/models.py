from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Material(models.Model):
    MATERIAL_TYPE = (
        ('file', 'Файл'),
        ('link', 'Посилання'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='materials')

    material_type = models.CharField(max_length=10, choices=MATERIAL_TYPE)

    file = models.FileField(upload_to='materials/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title