from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.books, name="books"),
    path("books/<int:id>/", views.bookdetail, name="book-detail"),
    path("books/<slug:slug_name>/", views.bookdetailname, name="book-detail-slug"),
    path("books/category/<int:category_id>/", views.getBooksByCategoryId, name="category_id"),
    path("books/category/<str:category_name>/", views.getBooksByCategory, name="category_name"),
    path("books/author/", views.getBooksByAuthor, name="author"),
    path("authors/", views.authors, name="authors"),
    path("categories/", views.categories, name="categories"),
]
