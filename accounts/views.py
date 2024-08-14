from django.shortcuts import render, HttpResponse,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
import hashlib
# Create your views here.

class LoginView(View):

    def get(self, request):
        return render(request, 'accounts/login.html')
    
    def post(self, request):
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        user = User.objects.filter(email = email)

        if not user.exists():
            messages.error(request,"Ivalid User")
            return redirect('login')
        
        username = user.first().username
        
        user = authenticate( request, username = username, password = password )

        if user is None:
            messages.error(request,"Invalid Password")
            return redirect('login')
        else:
            login(request,user)
            return redirect('home')

class RegisterView(View):

    def get(self, request):
        return render(request, 'accounts/register.html')
    
    def post(self, request):
        data = request.POST
        fname = data.get('first_name')
        lname = data.get('last_name')
        uname = data.get('user_name')
        password = data.get('password')
        repassword = data.get('repassword')

        if password != repassword:
            messages.error(request,"Password not Matched") #need to work more because message.tags = error instead of danger
            return redirect('register')

        user = User.objects.filter(username = uname)

        if user.exists():
            messages.error(request,"User already exists!")
            return redirect('register')

        user = User.objects.create(
            first_name = fname,
            last_name = lname,
            username = uname,
        )

        user.set_password(password)
        user.save()

        messages.success(request,"Account Created Successfully")

        return redirect('register')

