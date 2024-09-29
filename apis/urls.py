from django.urls import path
from . import views


urlpatterns = [
    path('newsfeed/', views.NewsFeedAPIView.as_view(), name='newsfeedapi'),
    path('profile/<str:username>/', views.UserProfileAPIView.as_view(), name='profileapi'),
]