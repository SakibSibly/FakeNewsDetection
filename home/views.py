from django.shortcuts import render
from django.views import View
# Create your views here.

class MainView(View):
    def showHomePage(request):
        return render(request, 'home/index.html')
    
    # def showAboutPage(request):
    #     return render(request, 'home/index.html')