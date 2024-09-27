from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.core.mail import send_mail
from .models import CustomUser
from .forms import UserRegistrationForm
import os


class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password, country=country, city=city)
            user.save()
            message = "Thank you for registering on our website!\n\n"
            message += "Your username is: " + username + "\n\n\n"
            message += "For any queries, please contact us at: " + os.environ.get('EMAIL_HOST_USER') + "\n"
            message += "We will be happy to help you!\n"
            message += "Thank you!"

            send_mail('Welcome to FakeNewsDetection website!', message, os.environ.get('EMAIL_HOST_USER'), [email])
            return redirect('login')
        return render(request, 'accounts/register.html', {'form': form})


class UserProfileView(View):
    def get(self, request, username):
        user = CustomUser.objects.get(username=username)
        return render(request, 'accounts/profile.html' , {'user': user})

    def post(self, request):
        pass


class UserProfileAPI(View):
    def get(self, request, username):
        user = CustomUser.objects.get(username=username)
        return JsonResponse({'user': user})
    
    def post(self, request):
        pass
