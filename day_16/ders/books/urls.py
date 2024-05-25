from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("create-book/", views.BookCreateView.as_view(), name="create-book"),
    path("book-list/", views.BookListView.as_view(), name="book-list"),
    path("book-edit/<slug:slug>/", views.BookEditView.as_view(), name="book-edit"),
    path("book-delete/<slug:slug>/", views.BookDeleteView.as_view(), name="book-delete"),
    path("authors/", views.authors, name="authors"),
    path("create-author/", views.AuthorCreateView.as_view(), name="create-author"),
    path("categories/", views.categories, name="categories"),
    path("upload/", views.upload, name="upload"),
    path("<slug:book_slug>/", views.BookDetailView.as_view(), name="book-detail"),# localhost:8000/books/dirilis
    path("<slug:slug_name>/", views.bookdetailname, name="book-detail-slug"),
    path("category/<slug:slug>/", views.CategoryBooksListView.as_view(), name="category_slug"),
    path("author/<slug:slug>/", views.getBooksByAuthor, name="author"),
    path("search", views.SearchView.as_view(), name="search"),
]
