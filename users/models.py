from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
"""
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('player', 'Player'),
        ('manager', 'Manager'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
"""

class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(
        verbose_name='Phone Number',
        max_length=15,
        unique=True,
        blank=False
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=datetime.now)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'is_staff', 'is_active', 'date_joined']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
