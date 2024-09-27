from django.shortcuts import render
from django.views import View

# Create your views here.
class Globals(View):
    def get(self,request):
        return render(request,'globals/base.html')
