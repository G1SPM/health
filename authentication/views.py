from django.shortcuts import render,redirect
from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from main.models import Customer

# Create your views here.
def register_user(request):
    form = RegisterUserForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                
                Customer.objects.create(
                    user = user,first_name = user.first_name,
                    last_name=user.last_name,
                    email = user.email
                )

                messages.success(request,'User Created')
                return redirect('loginUser')
        context = {'form':form}
        return render(request,'registration/register.html',context)
 
#@login_required(login_url="home")
def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
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