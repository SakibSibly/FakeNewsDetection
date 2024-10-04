from django.views import View
from django.urls import reverse
from django.http import JsonResponse
from django.utils.http import urlencode
from newsfeed.models import News
from accounts.models import CustomUser
from .models import APIRequest
from django.utils import timezone


class PopulateAPIDatabase():
    def populate(request, method, endpoint, status_code):
        if request.user.is_authenticated:
            new_request = APIRequest(user=request.user, method=method, endpoint=endpoint, status_code=status_code)
            new_request.save()
        else:
            new_request = APIRequest(user=None, method=method, endpoint=endpoint, status_code=status_code)
            new_request.save()


class NewsFeedAPIView(View):
    def get(self, request):
        news = News.objects.order_by("-created_at")[:5]
        
        data = {
            'title': 'News Feed API',
            'news': list(news.values()),
            'message': 'This is the news feed API endpoint.',
            'method': 'GET',
            'status': 200
        }

        PopulateAPIDatabase.populate(request, 'GET', '/newsfeed/', 200)

        return JsonResponse(data)


class NewsFeedDetailAPIView(View):
    def get(self, request, pk):
        news = News.objects.filter(pk=pk)
        
        data = {
            'title': 'News Feed Detail API',
            'news': list(news.values()),
            'message': f'This is the news feed detail API endpoint for {pk}.',
            'method': 'GET',
            'status': 200
        }

        PopulateAPIDatabase.populate(request, 'GET', f'/newsfeed/{pk}/', 200)

        return JsonResponse(data)


class UserProfileAPIView(View):
    def get(self, request, username):
        if request.user.is_authenticated:

            custom_user = CustomUser.objects.filter(username=username).first()

            data = {
                'title': 'User Profile API',
                'user': {
                    'username': custom_user.username,
                    'first_name': custom_user.first_name,
                    'last_name': custom_user.last_name,
                    'country': custom_user.country,
                    'city': custom_user.city,
                    },
                'message': f'This is the user profile API endpoint for {username}.',
                'method': 'GET',
                'status': 200
            }

            PopulateAPIDatabase.populate(request, 'GET', f'/profile/{username}/', 200)

            return JsonResponse(data)
        
        PopulateAPIDatabase.populate(request, 'GET', f'/profile/{username}/', 403)

        return JsonResponse({'message': 'You need to login to the system to get the data', 'status': 403})
