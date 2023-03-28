from django.shortcuts import render,redirect
from .forms import RegisterUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_user(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Created')
            return redirect('loginUser')
    context = {'form':form}
    return render(request,'registration/register.html',context)
 
#@login_required(login_url="home")
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username ,password = password)

        if user is not None:
            login(request,user)
            messages.success(request,'User Logged in')
            return redirect('home')
        else:
            messages.success(request,'Username or password is incorrect')

    return render(request,'login/login.html')

def logout_user(request):
    logout(request)
    return redirect('loginUser')