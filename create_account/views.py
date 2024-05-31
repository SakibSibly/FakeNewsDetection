from django.shortcuts import render
from django.views import View

# Create your views here.


class MainView(View):
    def create(request):
        return render(request, 'create_account/create.html')