from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from books.models import Category
from django.contrib.auth import authenticate, login, logout
from .forms import LoginUserForm, NewUserForm

# Create your views here.

def users(request):
    users = User.objects.all()
    kategoriler = Category.objects.all()
    
    return render(request, "users/users.html", {
        "users": users,
        "categories": kategoriler
    })
    
def user_login(request):
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
        
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return render(request, "user/login.html", {
                    "form": form,
                    "error": "username veya parola yanlış"
                    })
            
        else:
            return render(request, "users/login.html", {"form": form})
    else:
        form = LoginUserForm()
        return render(request, "users/login.html", {"form": form})
    
    
def user_logout(request):
    logout(request)
    return redirect("index")

def user_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("index")
        else:
            return render(request, "users/register.html", {"form": form})
    else:
        form = NewUserForm()
        return render(request, "users/register.html", {"form": form})