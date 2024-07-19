from django.shortcuts import render, HttpResponse
from django.views import View
from ml import CustomScraper as CS, SimilarityFinder as SF
# Create your views here.

class MainView(View):
    def requestHandler(request):
        if request.method == 'POST':
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
            
        return render(request, 'home/index.html')
    
    def showAboutPage(request):
        return HttpResponse("Implement the About us page with a new tab window")
