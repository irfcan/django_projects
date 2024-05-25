from django.urls import path
from . import views

urlpatterns = [
    path("", views.users, name="user"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.user_register, name="register"),
    path("change-password/", views.change_password, name="change-password"),
]