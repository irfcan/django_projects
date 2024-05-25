from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-book/", views.create_book, name="create-book"),
    path("book-list/", views.book_list, name="book-list"),
    path("book-edit/<slug:slug>/", views.book_edit, name="book-edit"),
    path("book-delete/<slug:slug>/", views.book_delete, name="book-delete"),
    path("authors/", views.authors, name="authors"),
    path("create-author/", views.author_create, name="create-author"),
    path("categories/", views.categories, name="categories"),
    path("upload/", views.upload, name="upload"),
    path("<slug:slug>/", views.bookdetail, name="book-detail"),# localhost:8000/books/dirilis
    path("<slug:slug_name>/", views.bookdetailname, name="book-detail-slug"),
    path("category/<slug:slug>/", views.getBooksByCategory, name="category_slug"),
    path("author/<slug:slug>/", views.getBooksByAuthor, name="author"),
    path("search", views.search, name="search"),
]
