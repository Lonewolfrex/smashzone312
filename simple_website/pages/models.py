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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    sports_nickname = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    sports_club_player = models.BooleanField(default=False)
    club_name_sports = models.CharField(max_length=100, blank=True)
    club_location_sports = models.CharField(max_length=200, blank=True)  # New field for location
    society_club_player = models.BooleanField(default=False)
    club_name_society = models.CharField(max_length=100, blank=True)
    club_location_society = models.CharField(max_length=200, blank=True)  # New field for location
    corporate_player = models.BooleanField(default=False)
    club_name_corporate = models.CharField(max_length=100, blank=True)
    club_location_corporate = models.CharField(max_length=200, blank=True)  

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
    
class Tournament(models.Model):
    PHASE_CHOICES = [
        ('announcement', 'Tournament Announcement and Promotion'),
        ('registration_open', 'Tournament Registration Open'),
        ('registration_close', 'Tournament Registration Close'),
        ('begin', 'Tournament Begin'),
        ('end', 'Tournament End'),
        ('ceremony', 'Tournament Ceremony'),
    ]

    name = models.CharField(max_length=100)
    date = models.DateField()
    phase = models.CharField(max_length=20, choices=PHASE_CHOICES, default='announcement')
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name