from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import UserProfile, Sport, UserSport



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'full_name',
            'email',
            'phone_number',
            'address',
            'sports_nickname',
            'profile_picture',
        ]

class UserSportForm(forms.ModelForm):
    class Meta:
        model = UserSport
        fields = ['sport', 'level']