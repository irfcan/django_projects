from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from users.forms import UserLoginForm, NewUserForm, UserPasswordChangeForm

# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("index")
            
            else:
                return render(request, "users/login.html", {"form": form})
        else:
            return render(request, "users/login.html", {"form": form})
    else:
        form = UserLoginForm()
        return render(request, "users/login.html", {"form": form})
    
    
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
    

def user_logout(request):
    logout(request)
    return redirect("index")

def change_password(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("change-password")
        
        else:
            return render(request, "users/change-password.html", {"form": form})
        
    else:
        form = UserPasswordChangeForm(request.user)
        return render(request, "users/change-password.html", {"form": form})