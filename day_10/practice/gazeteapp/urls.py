from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # http://localhost:8000/
    path("about/", views.about, name="about"),
    path("authors/", views.authors, name="authors"),
    path("authors/<slug:slug>/", views.author_details, name="author-detail"),
    path("<slug:slug>/", views.makale_details, name="makale-detail"),
    path("author/<slug:slug>/", views.getMakaleByAuthors, name="makale-by-author"),
]
