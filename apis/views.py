from django.shortcuts import render
from django.views import View
from django.http import JsonResponse


class NewsFeedAPIView(View):
    def get(self, request):
        data = {
            'title': 'News Feed API',
            'message': 'This is the news feed API endpoint.'
        }
        return JsonResponse(data)


class NewsFeedDetailAPIView(View):
    def get(self, request, pk):
        data = {
            'title': 'News Feed Detail API',
            'message': f'This is the news feed detail API endpoint for {pk}.'
        }
        return JsonResponse(data)


class UserProfileAPIView(View):
    def get(self, request, username):
        data = {
            'title': 'User Profile API',
            'message': f'This is the user profile API endpoint for {username}.'
        }
        return JsonResponse(data)