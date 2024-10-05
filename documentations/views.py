from django.shortcuts import render
from django.views import View


class DocumentationView(View):
    def get(self, request):
        return render(request, 'documentations/documentation.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'documentations/about.html')


class OverviewView(View):
    def get(self, request):
        return render(request, 'documentations/overview.html')



class CodeOfConductView(View):
    def get(self, request):
        return render(request, 'documentations/code_of_conduct.html')


class CookiePolicyView(View):
    def get(self, request):
        return render(request, 'documentations/cookie_policy.html')