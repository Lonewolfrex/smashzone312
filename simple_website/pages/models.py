# pages/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    # You may want to define roles differently
    roles = models.ManyToManyField('Role', blank=True, related_name='users')

    class Meta:
        permissions = [
            ('can_view_dashboard', 'Can view dashboard'),
        ]

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    sports_nickname = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class UserSport(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('audience', 'Audience'),
    ]

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    def __str__(self):
        return f"{self.user_profile.full_name} - {self.sport.name} ({self.level})"
    

