from django.shortcuts import render
from django.views import View

# Create your views here.


class MainView(View):
    def showCreatePage(request):
        return render(request, 'create/index.html')