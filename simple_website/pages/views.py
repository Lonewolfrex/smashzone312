# pages/views.py

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import get_user_model
from .models import Role
from datetime import datetime
from .models import UserProfile, Sport, UserSport
from .forms import UserProfileForm, UserSportForm

def index(request):
    return render(request, 'pages/index.html')

def register(request):
    User = get_user_model()  # Get the custom user model
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        roles = request.POST.getlist('roles')  # Get the selected roles

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists. Please choose a different one.'
            return render(request, 'pages/register.html', {'error_message': error_message})

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            error_message = 'Email already exists. Please use a different email.'
            return render(request, 'pages/register.html', {'error_message': error_message})

        # Check if password and confirm password match
        if password != confirm_password:
            error_message = 'Passwords do not match.'
            return render(request, 'pages/register.html', {'error_message': error_message})

        # Create the user if all checks pass
        user = User.objects.create_user(username=username, password=password, email=email)
        user.phone_number = phone_number
        user.save()

        # Assign roles to the user
        for role_name in roles:
            role, created = Role.objects.get_or_create(name=role_name)  # Get or create the role
            user.roles.add(role)  # Add the role to the user

        return redirect('login')  # Redirect to the login page after successful registration

    return render(request, 'pages/register.html')  # Render the registration form

def login_view(request):  # Ensure this function is defined
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        # Check if the user is authenticated
        if user is not None:
            auth_login(request, user)  # Correctly pass the request and user
            return redirect('dashboard')  # Redirect to the dashboard after login
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = ''
    
    return render(request, 'pages/login.html', {'error_message': error_message})

def dashboard(request):
    if request.user.is_authenticated:
        current_year = datetime.now().year
        return render(request, 'pages/dashboard.html', {'current_year': current_year})
    else:
        return redirect('login') # Redirect to login if user is not authenticated

def logout_view(request):
    logout(request)
    return redirect('index')

def user_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    sports = Sport.objects.all()  # Fetch all sports from the database

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if profile_form.is_valid():
            profile_form.save()  # Save the profile details

            # Save player types and club names
            profile.sports_club_player = request.POST.get('sports_club_player') == 'on'
            profile.club_name_sports = request.POST.get('club_name_sports', '')
            profile.society_club_player = request.POST.get('society_club_player') == 'on'
            profile.club_name_society = request.POST.get('club_name_society', '')
            profile.corporate_player = request.POST.get('corporate_player') == 'on'
            profile.club_name_corporate = request.POST.get('club_name_corporate', '')
            profile.save()  # Save the updated profile

            # Process selected sports and levels
            selected_sports = request.POST.getlist('sports')  # Get the selected sports
            for sport_id in selected_sports:
                sport = Sport.objects.get(id=sport_id)
                level = request.POST.get(f'level_{sport.id}')  # Ensure this matches your input name
                if level:
                    user_sport, created = UserSport.objects.get_or_create(
                        user_profile=profile,
                        sport=sport,
                        defaults={'level': level}
                    )
                    if not created:
                        user_sport.level = level  # Update level if already exists
                        user_sport.save()

            return redirect('view_profile')  # Redirect to the view profile page after saving
    else:
        profile_form = UserProfileForm(instance=profile)
        print(profile_form.errors)
    user_sports = UserSport.objects.filter(user_profile=profile)

    return render(request, 'pages/user_profile.html', {
        'profile_form': profile_form,
        'user_sports': user_sports,
        'sports': sports,  # Pass the sports to the template
    })
    
def view_profile(request):
    profile = UserProfile.objects.get(user=request.user)  # Get the user's profile
    user_sports = UserSport.objects.filter(user_profile=profile)  # Get all sports associated with the profile

    return render(request, 'pages/view_profile.html', {
        'profile': profile,
        'user_sports': user_sports,
    })

def navigate_user_profile(request):
    # Check if the user has a profile
    if hasattr(request.user, 'profile'):
        # If the profile exists, redirect to the View Profile page
        return redirect('view_profile')
    else:
        # If the profile does not exist, redirect to the User Profile page
        return redirect('user_profile')

def tournament_calendar(request):
    # Logic for user profile
    return render(request, 'pages/tournament_calendar.html') 

def sports_update(request):
    # Logic for user profile
    return render(request, 'pages/sports_update.html') # Redirect to the index page after logout