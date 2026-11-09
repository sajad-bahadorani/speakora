from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        SUPER_ADMIN = 'super_admin', 'Super Admin'
        MANAGER = 'manager', 'Manager'
        EDUCATIONAL_MANAGER = 'educational_manager', 'Educational Manager'
        OBSERVER = 'observer', 'Observer'
        TEACHER = 'teacher', 'Teacher'
        STUDENT =  'student', 'Student'

    role = models.CharField(
        max_length=30,
        choices=Role.choices,
        default=Role.STUDENT
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to='users/profile_pictures/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

