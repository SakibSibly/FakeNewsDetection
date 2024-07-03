from django.shortcuts import render, HttpResponse
from django.views import View
from ml import CustomScraper as CS, SimilarityFinder as SF
# Create your views here.

class MainView(View):
    def showHomePage(request):
        # THE REQUEST MAY CONFLICT WITH PRINT FEATURE
        if request.method == 'POST':
            query = request.POST.get('query')
            customScraper = CS.CustomScraeper(query)
            customScraper.getNews()
            similarityFinder = SF.SimilarityFinder(query)
            similarityFinder.findSimilarity()
            output = open('ml/final_output.txt', 'r', encoding='utf-8').read()
            return render(request,'home/show.html',context={'content':output})
            
        return render(request, 'home/index.html')
    
    def showAboutPage(request):
        pass
