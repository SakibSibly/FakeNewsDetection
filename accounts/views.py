from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core.mail import send_mail
from .models import CustomUser, MailingHistory
from .forms import UserRegistrationForm
import os
from pathlib import Path
import environ


class UserRegistrationView(View):
    def __init__(self):
        self.env = environ.Env()
        BASE_DIR = Path(__file__).resolve().parent.parent
        environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

    def get(self, request):
        # return HttpResponse(os.environ)

        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']

            if CustomUser.objects.filter(username=username).exists():
                return render(request, 'accounts/register.html', {'form': form, 'error': 'Username is not available'})
            if CustomUser.objects.filter(email=email).exists():
                return render(request, 'accounts/register.html', {'form': form, 'error': 'Email already used by another user'})
            if len(password) < 8:
                return render(request, 'accounts/register.html', {'form': form, 'error': 'Password must be at least 8 characters long'})
            if password != confirm_password:
                return render(request, 'accounts/register.html', {'form': form, 'error': 'Password and Confirm Password do not match'})

            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password, country=country, city=city)
            user.save()

            try:
                message = "Thank you for registering on our website!\n\n"
                message += "Your username is: " + username + "\n\n\n"
                message += "For any queries, please contact us at: " + self.env('EMAIL_HOST_USER') + "\n"
                message += "We will be happy to help you!\n"
                message += "Thank you!"

                subject = 'Welcome to FakeNewsDetection website!'

                send_mail(subject, message, self.env('EMAIL_HOST_USER'), [email])

                mailing_history = MailingHistory(user=user, email_subject=subject, email_body=message)
                mailing_history.save()
            except Exception as e:
                mailing_history = MailingHistory(user=user, email_subject='Failed to send email', email_body=str(e))
                mailing_history.save()

            return redirect('login')
        return render(request, 'accounts/register.html', {'form': form})


class UserProfileView(View):
    def get(self, request, username):
        user = CustomUser.objects.get(username=username)
        return render(request, 'accounts/profile.html' , {'user': user})

    def post(self, request):
        pass


class PrintView(View):
    def get(self, request):
        return HttpResponse("Printed report not available yet!")
