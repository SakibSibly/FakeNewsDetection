from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('profile/<str:username>/', views.UserProfileView.as_view(), name='profile'),
    path('print/', views.PrintView.as_view(), name='print_report'),
    path('history/<str:username>/', views.UserHistoryView.as_view(), name='history'),
]