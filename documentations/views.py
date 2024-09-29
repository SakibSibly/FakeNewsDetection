from django.shortcuts import render
from django.views import View


class DocumentationView(View):
    def get(self, request):
        return render(request, 'documentations/documentation.html')
    
    def post(self, request):
        pass
