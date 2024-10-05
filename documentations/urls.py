from django.urls import path
from . import views


urlpatterns = [
    path('documetation/', views.DocumentationView.as_view(), name='documentation'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('overview/', views.OverviewView.as_view(), name='overview'),
    path('code_of_conduct/', views.CodeOfConductView.as_view(), name='code_of_conduct'),
    path('cookie_policy/', views.CookiePolicyView.as_view(), name='cookie_policy'),
]