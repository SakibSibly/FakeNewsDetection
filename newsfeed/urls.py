from django.urls import path
from . import views


urlpatterns = [
    path('newsfeed/', views.NewsFeedView.as_view(), name='news_feed'),
    path('newsfeed/<int:pk>/', views.NewsFeedDetailView.as_view(), name='news_feed_detail'),
]