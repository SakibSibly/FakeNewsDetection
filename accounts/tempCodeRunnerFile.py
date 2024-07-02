from django.shortcuts import render, HttpResponse
# from django.views import View
# from accounts.models import User
# # Create your views here.

# class MainView(View):
#     def showLoginPage(request):
#         return render(request, 'accounts/login.html')
    
#     def showRegisterPage(request):
#         if request.method == 'POST':
#             data = request.POST
#             name = data.get('name')
#             uname = data.get('uname')
#             email = data.get('email')
#             password = data.get('password')

#             newUser = User(
#                 name = name,
#                 username = uname,
#                 email = email,
#                 password = password,
#             )
#             newUser.save()
#             data = User.objects.all()
#             return render(request, 'accounts/success.html')

#         return render(request, 'accounts/register.html')