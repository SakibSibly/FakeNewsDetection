from django.shortcuts import render
from django.views import View
# Create your views here.

class MainView(View):
    def login(request):
        return render(request, 'login/index.html')