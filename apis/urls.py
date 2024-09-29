from django.urls import path
from . import views


urlpatterns = [
    path('newsfeed/', views.NewsFeedAPIView.as_view(), name='news_feed_api'),
    path('newsfeed/<int:pk>/', views.NewsFeedDetailAPIView.as_view(), name='news_feed_detail_api'),
    path('profile/<str:username>/', views.UserProfileAPIView.as_view(), name='profile_api'),
]