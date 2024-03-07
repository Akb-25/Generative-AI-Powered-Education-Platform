from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import RegisterForm,LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,"core/home.html")
def register(request):
    form=RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    context={'registerform':form}
    return render(request,"core/register.html",context=context)

def login(request):
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("dashboard")
    context={"loginform":form}
    return render(request,"core/login.html",context=context)

def logout(request):
    auth.logout(request)
    return redirect("")

@login_required(login_url="login")
def dashboard(request):
    return render(request,"core/dashboard.html")