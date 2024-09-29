from django.shortcuts import render
from django.views import View


class NewsFeedView(View):
    def get(self, request):
        return render(request, 'newsfeed/newsfeed.html')
    
    def post(self, request):
        pass
