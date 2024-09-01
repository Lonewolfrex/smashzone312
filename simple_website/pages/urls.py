# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),  # Ensure this line exists
    path('tournament_calendar/', views.tournament_calendar, name='tournament_calendar'),
    path('sports_update/', views.sports_update, name='sports_update'),
]