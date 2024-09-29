from django.urls import path
from . import views


urlpatterns = [
    path('newsfeed/', views.NewsFeedView.as_view(), name='newsfeed'),
    path('newsfeed/<int:pk>/', views.NewsFeedDetailView.as_view(), name='newsfeed_detail'),
]