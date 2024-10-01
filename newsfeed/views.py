from django.shortcuts import render
from django.views import View
from .models import News


class NewsFeedView(View):
    def get(self, request):
        return render(request, 'newsfeed/newsfeed.html')


class NewsDetailView(View):
    def get(self, request, pk):
        news = News.objects.filter(pk=pk).first()
        return render(request, 'newsfeed/individual_newsfeed.html', {'news': news})
