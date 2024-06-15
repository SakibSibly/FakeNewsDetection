from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.

class MainView(View):
    def showLoginPage(request):
        return render(request, 'accounts/login.html')
    
    def showRegisterPage(request):
        return render(request, 'accounts/register.html')