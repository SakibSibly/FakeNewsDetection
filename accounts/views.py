from django.shortcuts import render, HttpResponse,redirect
from django.views import View
from accounts.models import User
import hashlib
# Create your views here.

class LoginView(View):

    def get(self, request):
        return render(request, 'accounts/login.html')
    
    def post(self, request):
        data = request.POST
        email = data.get('email')
        password = hashlib.sha256(data.get('password').encode()).hexdigest()

        database = User.objects.all()
        for user in database:
            if user.email == email and user.password == password:
                return redirect('home')
        
        return render(request, 'accounts/unsuccessful_login.html')

class RegisterView(View):

    def get(self, request):
        return render(request, 'accounts/register.html')
    
    def post(self, request):
        data = request.POST
        name = data.get('name')
        uname = data.get('uname')
        email = data.get('email')
        password = hashlib.sha256(data.get('password').encode()).hexdigest()

        newUser = User(
            name = name,
            username = uname,
            email = email,
            password = password,
        )
        newUser.save()
        return render(request, 'accounts/success.html')
