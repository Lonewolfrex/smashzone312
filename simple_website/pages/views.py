# pages/views.py

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import get_user_model
from .models import Role
from datetime import datetime
from .models import UserProfile, Sport, UserSport
from .forms import UserProfileForm

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

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        
        # Process sports and levels
        for sport in Sport.objects.all():
            level = request.POST.get(f'level_{sport.id}')  # Get the level for each sport
            if level:
                user_sport, created = UserSport.objects.get_or_create(
                    user_profile=profile,
                    sport=sport,
                    defaults={'level': level}
                )
                if not created:
                    user_sport.level = level  # Update level if already exists
                    user_sport.save()

        if profile_form.is_valid():
            profile_form.save()
            return redirect('user_profile')  # Redirect to the same page after saving
    else:
        profile_form = UserProfileForm(instance=profile)

    sports = Sport.objects.all()  # Get all available sports
    user_sports = UserSport.objects.filter(user_profile=profile)  # Get user's sports

    # Prepare a dictionary to hold user sports and levels
    user_sport_levels = {user_sport.sport.id: user_sport.level for user_sport in user_sports}

    return render(request, 'pages/user_profile.html', {
        'profile_form': profile_form,
        'sports': sports,
        'user_sport_levels': user_sport_levels,  # Pass the dictionary to the template
    })


def tournament_calendar(request):
    # Logic for user profile
    return render(request, 'pages/tournament_calendar.html') 

def sports_update(request):
    # Logic for user profile
    return render(request, 'pages/sports_update.html') # Redirect to the index page after logout