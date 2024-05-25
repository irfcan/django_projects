from django.urls import path
from phoneBook import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]