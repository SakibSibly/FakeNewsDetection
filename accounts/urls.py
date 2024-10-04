from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('profile/<str:username>/', views.UserProfileView.as_view(), name='profile'),
    # path('print/', views.PrintReportView.as_view(), name='print_report'),
    path('print/<int:pk>/', views.PrintReportView.as_view(), name='print_report'),
    path('history/<str:username>/', views.UserHistoryView.as_view(), name='history'),
    
    # Password reset request (Forgot Password)
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), 
        name='password_reset'),

    # Password reset email sent
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), 
        name='password_reset_done'),

    # Password reset confirmation link
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), 
        name='password_reset_confirm'),

    # Password successfully reset
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), 
        name='password_reset_complete'),
]