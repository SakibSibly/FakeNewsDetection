from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core.mail import send_mail
from .models import CustomUser, MailingHistory, SearchData
from .forms import UserRegistrationForm
from reportlab.pdfgen import canvas
import os
from pathlib import Path
import environ


class UserRegistrationView(View):
    def __init__(self):
        self.env = environ.Env()
        BASE_DIR = Path(__file__).resolve().parent.parent
        environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

    def get(self, request):
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


class UserHistoryView(View):
    def get(self, request, username):
        if request.user.is_authenticated and request.user.username == username:
            history = SearchData.objects.filter(user__username=username)
            return render(request, 'accounts/history.html', {'history': history})
        
        return HttpResponse('Unauthorized access!')


class PrintReportView(View):
    def get(self, request, pk):

        # fetched_data = SearchData.objects.order_by('-date')[0]
        fetched_data = SearchData.objects.filter(pk=pk)[0]

        heading = "News Detection Result\n\n"
        
        query = "Search Data:\n" + fetched_data.search_data   
        verdict = fetched_data.verdict
        
        meta_data = "\n\n\nThank you for using our service!\n"
        meta_data += "For any queries, please contact us at the feedback section\n"
        meta_data += "We will be happy to help you!\n"
        meta_data += "Thank you!\n"
        meta_data += "FND Team\n\n"
        meta_data += "*Truth is learned, never told!"


        if verdict == '1':
            verdict = "Analysis Result:\n" + "Fake News!"

        elif verdict == '0':
            verdict = "Analysis Result:\n" + "Real News!"

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="News_Detection_Result.pdf"'

        pdf = canvas.Canvas(response)


        x = 100
        y = 800


        y = self.draw_text(pdf, heading, x + x + x / 2.5, y) # Static Adjustment
        y = self.draw_text(pdf, query, x, y)
        y = self.draw_text(pdf, verdict, x, y - 40)
        y = self.draw_text(pdf, meta_data, x, y - 40)

        pdf.showPage()
        pdf.save()

        return response
    
    def draw_text(self, pdf, text, x, y):
        for line in text.split('\n'):
            pdf.drawString(x, y, line)
            y -= 20  # Move y coordinate for the next line
        return y
