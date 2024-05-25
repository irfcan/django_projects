from django.forms import BaseForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from books.models import Category
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import LoginUserForm, NewUserForm, UserPasswordChangeForm
from django.contrib import messages
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


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
    
    
class UserLoginView(FormView):
    template_name = "users/login.html"
    form_class = LoginUserForm
    success_url = reverse_lazy("index")
    
    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, "Giriş Başarılı")
            return super().form_valid(form)
        else:
            messages.add_message(self.request, messages.ERROR, "username veya parola yanlış")
            return self.form_invalid(form)
    
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
    

class UserRegisterView(SuccessMessageMixin, FormView):
    template_name = "users/register.html"
    form_class = NewUserForm
    success_url = reverse_lazy("index")
    success_message = "Kayıt işlemi başarıyla tamamlandı."
    
    def form_valid(self, form):
        form.save()
        
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        
        user = authenticate(self.request, username=username, password=password)
        
        login(self.request, user)
        
        return super().form_valid(form)

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

class ChangePasswordView(FormView):
    template_name = "users/change-password.html"
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("change-password")
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        messages.success(self.request, "Parolanız Güncellendi!")
        return super().form_valid(form)