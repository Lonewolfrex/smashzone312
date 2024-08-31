# pages/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    # You may want to define roles differently
    roles = models.ManyToManyField('Role', blank=True, related_name='users')

    class Meta:
        permissions = [
            ('can_view_dashboard', 'Can view dashboard'),
            # Add other custom permissions here if needed
        ]

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name