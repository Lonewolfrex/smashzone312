# pages/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.navigate_user_profile, name='navigate_user_profile'),
    path('tournament_calendar/', views.tournament_calendar, name='tournament_calendar'),
    path('sports_update/', views.sports_update, name='sports_update'),
    path('view-profile/', views.view_profile, name='view_profile'),
    path('user-profile/', views.user_profile, name='user_profile'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)