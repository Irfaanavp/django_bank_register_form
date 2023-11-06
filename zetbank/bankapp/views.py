from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import Userform
from .forms import UserForm
from django.contrib.auth import logout
# Create your views here.
def index(request):
    return render(request, 'index.html')


# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm = request.POST['confirm']
#         if password == confirm:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, "username exist")
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, "email exist")
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username,
#                                                 email=email,
#                                                 password=password)
#                 user.save();
#             return redirect('login')
#         else:
#             messages.info(request, "password not matching")
#             return redirect('register')
#         return redirect('/')
#     return render(request, 'register.html')
def register(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm = request.POST.get('confirm', '')
        if not username or not password or not confirm:
            return render(request, 'register.html', {'error': 'All fields are required.'})

        if request.POST['password'] == request.POST['confirm']:
              try:
                User.objects.get(username = request.POST['username']).exists()
                return render (request,'register.html', {'error':'Username is already taken!'})
              except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password'])
                auth.login(request,user)
                return redirect('login')
        else:
            return render (request,'register.html', {'error':'Password does not match!'})
    else:
        return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            return render(request, 'login.html', {'error': 'invalied user name or password!'})
            # messages.info(request, "invalid credential")
            return redirect('login')
    return render(request, 'login.html')

def new(request):

    return render(request,'new.html')

def form(request):
    message=None
    if request.method == 'POST':
        form= UserForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Application accepted'
            return redirect('success')
            # Display a success message and redirect to the home page.
            # return render(request, 'success.html', {'message': 'Application accepted'})
    else:
        form= Userform()
        messages.error(request, 'Invalid form data. Please check your inputs.')
    return render(request, 'form.html', {'form': form,'message':message})

def success(request):
    return render(request,'success.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def a(request):
    return render(request,'a.html')