# pages/views.py

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import get_user_model
from .models import Role

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
        return render(request, 'pages/dashboard.html')
    else:
        return redirect('login')  # Redirect to login if user is not authenticated

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to the index page after logout