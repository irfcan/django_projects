from django.urls import path
from . import views

urlpatterns = [
    path("", views.users, name="user"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("change-password/", views.ChangePasswordView.as_view(), name="change-password"),
]