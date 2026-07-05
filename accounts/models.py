from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('admin', 'Admin'),)

    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='student')
    profile_picture = models.ImageField(upload_to='profiles/',blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username