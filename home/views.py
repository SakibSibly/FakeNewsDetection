from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin,View):
    
    login_url='login'

    def get(self, request):
        return render(request, 'home/home.html')
    
    # def post(self, request):
        form_type = request.POST.get('form_type')
        if form_type == 'check_news':
            query = request.POST.get('query')
            customScraper = CS.CustomScraeper(query)
            customScraper.getNews()
            similarityFinder = SF.SimilarityFinder(query)
            similarityFinder.findSimilarity()
            output = open('ml/final_output.txt', 'r', encoding='utf-8').read()
            return render(request,'home/show.html',context={'content':output})
        elif form_type == 'print_report':
            # implement print feature
            return HttpResponse("Print feature is not implemented yet!")

class Profile(LoginRequiredMixin,View):

    login_url='login'

    def get(self, request):
        return self.logout_page(request)

    def logout_page(self, request):
        logout(request)
        return redirect('login')
