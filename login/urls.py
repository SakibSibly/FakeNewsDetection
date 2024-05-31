from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.showLoginPage, name='login'),
]