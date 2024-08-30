# pages/views.py

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'pages/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists. Please choose a different one.'
            return render(request, 'pages/register.html', {'error_message': error_message})

        # Create the user if the username is unique
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')  # Redirect to the login page after successful registration

    return render(request, 'pages/register.html')  # Render the registration form

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        # Check if the user is authenticated
        if user is not None:
            login(request, user)  # Pass the request and user to the login function
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