from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MainView.showLoginPage, name='login'),
    path('register/', views.MainView.showRegisterPage, name='register'),
]