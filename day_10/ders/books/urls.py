from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("authors/", views.authors, name="authors"),
    path("categories/", views.categories, name="categories"),
    path("<slug:slug>/", views.bookdetail, name="book-detail"),# localhost:8000/books/dirilis
    path("<slug:slug_name>/", views.bookdetailname, name="book-detail-slug"),
    path("category/<slug:slug>/", views.getBooksByCategory, name="category_slug"),
    path("author/<slug:slug>/", views.getBooksByAuthor, name="author"),
    path("search", views.search, name="search"),
]
