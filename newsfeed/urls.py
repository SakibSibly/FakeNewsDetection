from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsFeedView.as_view(), name='news_feed'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
]