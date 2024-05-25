from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # http://localhost:8000/
    path("about/", views.about, name="about"),
    path("authors/", views.authors, name="authors"),
]
