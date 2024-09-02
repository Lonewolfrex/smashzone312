from django import forms
from .models import UserProfile, Sport, UserSport

class UserProfileForm(forms.ModelForm):
    sports_club_player = forms.BooleanField(required=False, label="Sports Club Player")
    society_club_player = forms.BooleanField(required=False, label="Society Club Player")
    corporate_player = forms.BooleanField(required=False, label="Corporate Player")

    club_name = forms.CharField(required=False, label="Enter the name of the club/society/corporate", max_length=100)

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
            'society_club_player',
            'corporate_player',
            'club_name',
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