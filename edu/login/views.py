from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm,LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def login(response):
    if response.method == "POST":
        form = LoginForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = LoginForm()
    return render(response, "login/login.html", {"form": form})

def register(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = RegisterForm()
    return render(request, 'login/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,usernmae=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("login")
        else:
            return render(request,'login.html',{"error_message":"Invalid login"})
    else:
        return render(request,"login.html")

def user_logout(request):
    logout(request)
    return redirect("login")