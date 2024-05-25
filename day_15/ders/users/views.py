from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from books.models import Category
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import LoginUserForm, NewUserForm, UserPasswordChangeForm
from django.contrib import messages


# Create your views here.

def users(request):
    users = User.objects.all()
    kategoriler = Category.objects.all()
    
    return render(request, "users/users.html", {
        "users": users,
        "categories": kategoriler
    })
    
def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        messages.add_message(request, messages.ERROR, "yetkiniz yok")
        return render(request, "users/login.html")
    
    
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
        
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Giriş Başarılı")
                
                nextURL = request.GET.get("next", None)
                if nextURL is None:
                    return redirect("index")
                else:
                    return redirect(nextURL)
            else:
                messages.add_message(request, messages.ERROR, "username veya parola yanlış")
                return render(request, "user/login.html")
            
        else:
            return render(request, "users/login.html", {"form": form})
    else:
        form = LoginUserForm()
        return render(request, "users/login.html", {"form": form})
    
    
def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Güvenle Çıkıldı")
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
    

def change_password(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # IMPORTANT
            return redirect("change-password")
        else:
            return render(request, "users/change-password.html", {"form": form})
        
    else:    
        form = UserPasswordChangeForm(request.user)
    return render(request, "users/change-password.html", {"form": form})