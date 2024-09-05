from django import forms
from .models import UserProfile, Sport, UserSport

class UserProfileForm(forms.ModelForm):
    sports_club_player = forms.BooleanField(required=False, label="Sports Club Player")
    society_club_player = forms.BooleanField(required=False, label="Society Club Player")
    corporate_player = forms.BooleanField(required=False, label="Corporate Player")

    club_name_sports = forms.CharField(required=False, label="Enter the name of the Sports Club", max_length=100)
    club_location_sports = forms.CharField(required=False, label="Enter the location of the Sports Club", max_length=200)  # New field
    club_name_society = forms.CharField(required=False, label="Enter the name of the Society Club", max_length=100)
    club_location_society = forms.CharField(required=False, label="Enter the location of the Society Club", max_length=200)  # New field
    club_name_corporate = forms.CharField(required=False, label="Enter the name of the Corporate Club", max_length=100)
    club_location_corporate = forms.CharField(required=False, label="Enter the location of the Corporate Club", max_length=200)  # New field

    class Meta:
        model = UserProfile
        fields = [
            'full_name',
            'email',
            'phone_number',
            'address',
            'sports_nickname',
            'profile_picture',
            'sports_club_player',
            'club_name_sports',
            'club_location_sports',  # Include new field
            'society_club_player',
            'club_name_society',
            'club_location_society',  # Include new field
            'corporate_player',
            'club_name_corporate',
            'club_location_corporate',  # Include new field
        ]

class UserSportForm(forms.ModelForm):
    sport = forms.ModelChoiceField(queryset=Sport.objects.all(), required=True, label="Select Sport")
    level = forms.ChoiceField(choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('audience', 'Audience'),
    ], required=True, label="Select Experience Level")

    class Meta:
        model = UserSport
        fields = ['sport', 'level']