from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core.mail import send_mail
from .models import CustomUser, MailingHistory
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

            try:
                message = "Thank you for registering on our website!\n\n"
                message += "Your username is: " + username + "\n\n\n"
                message += "For any queries, please contact us at: " + os.environ.get('EMAIL_HOST_USER') + "\n"
                message += "We will be happy to help you!\n"
                message += "Thank you!"

                subject = 'Welcome to FakeNewsDetection website!'

                send_mail(subject, message, os.environ.get('EMAIL_HOST_USER'), [email])

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
