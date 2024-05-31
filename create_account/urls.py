from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.create, name='create'),
    # path('create_account/', views.MainView.create_account, name='create_account'),
    # path('create_account_success/', views.MainView.create_account_success, name='create_account_success'),
]