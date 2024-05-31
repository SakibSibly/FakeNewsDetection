from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.home, name='main'),
]