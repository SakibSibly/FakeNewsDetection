from django.views import View
from django.urls import reverse
from django.http import JsonResponse
from django.utils.http import urlencode
from newsfeed.models import News
from accounts.models import CustomUser
from .models import APIRequest


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

        new_request = APIRequest(user=request.user, method='GET', endpoint='/newsfeed/', status_code=200)
        new_request.save()

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

        new_request = APIRequest(user=request.user, method='GET', endpoint=f'/newsfeed/{pk}/', status_code=200)
        new_request.save()

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

            new_request = APIRequest(user=request.user, method='GET', endpoint=f'/profile/{username}/', status_code=200)
            new_request.save()

            return JsonResponse(data)
        
        new_request = APIRequest(user=request.user, method='GET', endpoint=f'/profile/{username}/', status_code=403)

        login_url = reverse('login') + '?' + urlencode({'next': request.path})
        return JsonResponse({'message': 'You need to login to the system to get the data', 'status': 403})
