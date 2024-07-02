from django.shortcuts import render
from django.views import View
# Create your views here.

class MainView(View):
    def showHomePage(request):
        if request.method == 'POST':
            query = request.POST.get('query')
            return render(request,'home/show.html',context={'content':query})

        return render(request, 'home/index.html')
    
    # def showAboutPage(request):
    #     return render(request, 'home/index.html')