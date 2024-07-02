from django.shortcuts import render, HttpResponse,redirect
from django.views import View
from accounts.models import User
# Create your views here.

class MainView(View):
    def showLoginPage(request):
        if request.method == 'POST':
            data = request.POST
            email = data.get('email')
            password = data.get('password')

            database = User.objects.all()
            for user in database:
                if user.email == email and user.password == password:
                    return redirect('home')

        return render(request, 'accounts/login.html')
    
    def showRegisterPage(request):
        if request.method == 'POST':
            data = request.POST
            name = data.get('name')
            uname = data.get('uname')
            email = data.get('email')
            password = data.get('password')

            newUser = User(
                name = name,
                username = uname,
                email = email,
                password = password,
            )
            newUser.save()
            return render(request, 'accounts/success.html')

        return render(request, 'accounts/register.html')
    
