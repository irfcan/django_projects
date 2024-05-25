from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from account.forms import CreateUserForm, LoginForm, UpdateUserForm
from base64 import urlsafe_b64encode
from django.utils.encoding import force_bytes, force_str
from account.token import user_tokenizer_generate
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class RegisterView(FormView):
    template_name = "account/registration/register.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("email-verification-sent")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = self.request.get_current_site()
        
        subject = "Hesap doğrulama e-postası"
        
        message = self.render_to_string("account/registration/email-verification.html", {
            "user": user,
            "domain": current_site.domain,
            "uid": urlsafe_b64encode(force_bytes(user.pk)),
            "token": user_tokenizer_generate.make_token(user)
        })
        
        user.email_user(subject=subject, message=message)
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)
    

class EmailVerificationView(View):
    template_name = "account/registration/email-verification.html"
    
    def get(self, request, uidb64, token, *args, **kwargs):
        unique_id = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=unique_id)

        if user and user_tokenizer_generate.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect("email-verification-success")
        else:
            return redirect("email-verification-failed")
        
        
class EmailVerificationSentView(TemplateView):
    template_name = "account/registration/email-verification-sent.html"
    
class EmailVerificationSuccessView(TemplateView):
    template_name = "account/registration/email-verification-success.html"
    
class EmailVerificationFailedView(TemplateView):
    template_name = "account/registration/email-verification-failed.html"


class LoginView(FormView):
    template_name = "account/my-login.html"
    form_class = LoginForm
    
    def form_valid(self, form):
        
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            return redirect("dashboard")
        
        return super().form_invalid(form)
    
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "account/dashboard.html"
    
    
class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        request.session.flush()
        return redirect("store")
    

class ProfileManagementView(LoginRequiredMixin, UpdateView):
    template_name = "account/profile-management.html"
    
    form_class = UpdateUserForm
    
    success_url = reverse_lazy("dashboard")
    
    def get_object(self, queryset=None):
        return self.request.user
    
class DeleteAccountView(LoginRequiredMixin, DeleteView):
    
    template_name = "account/delete-account.html"
    
    success_url = reverse_lazy("store")
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        
        else:
            return redirect("store")