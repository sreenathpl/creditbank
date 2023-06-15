from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse

from appBank.models import user


def home(request):
    return render(request,"index.html")

def reglogin(request):
    password = None
    conf_password = None
    username = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        conf_password = request.POST['conf_password']
    if password == conf_password:
        if user.objects.filter(username = username).exists():
            messages.info(request,"Username already exists")
            return redirect('register')
        else:
            User = user.objects.create(username = username,
                                        password = password,)
            User.save()
            return render(request, "login.html")
    else:
        messages.info(request, "Password not matching")
        return render(request, "register.html")

def register(request):
    return render(request,"register.html")

def user_login(request):
    User = None
    if request.method == "POST":
        print("Inside post")
        user_name = request.POST['user_name']
        password = request.POST['password']
        User = user.objects.filter(username = user_name,
                                 password = password)
        print(User)
        if User:
            print("Login")
            request.session["isLoggedIn"] = True
            request.session["username"] = request.POST.get("user_name")
            return redirect("/")
        else:
            print("Not Login")
            messages.info(request,"Incorrect credentials")
            return render(request, "login.html")
    return render(request, "login.html")

def user_logout(request):
    request.session["isLoggedIn"] = False
    return redirect("/")

def cm_register(request):
    if request.method == "POST":
        messages.info(request,"Application Accepted")
    return render(request, "cm_register.html")
# Create your views here.
