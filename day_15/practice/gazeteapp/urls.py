from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # http://localhost:8000/
    path("makale-create/", views.makale_create, name="makale-create"),
    path("makale-list/", views.makale_list, name="makale-list"),
    path("makale-edit/<slug:slug>/", views.makale_edit, name="makale-edit"),
    path("makale-delete/<slug:slug>/", views.makale_delete, name="makale-delete"),
    path("about/", views.about, name="about"),
    path("authors/", views.authors, name="authors"),
    path("authors/<slug:slug>/", views.author_details, name="author-detail"),
    path("<slug:slug>/", views.makale_details, name="makale-detail"),
    path("author/<slug:slug>/", views.getMakaleByAuthors, name="makale-by-author"),
    path("search", views.search, name="search"),
]
