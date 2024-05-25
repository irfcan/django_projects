from django.urls import path
from . import views

urlpatterns = [
    path("", views.books, name="books"),
    path("authors/", views.authors, name="authors"),
    path("categories/", views.categories, name="categories"),
    path("<int:id>/", views.bookdetail, name="book-detail"),
    path("<slug:slug_name>/", views.bookdetailname, name="book-detail-slug"),
    path("category/<int:category_id>/", views.getBooksByCategoryId, name="category_id"),
    path("category/<str:category_name>/", views.getBooksByCategory, name="category_name"),
    path("author/<slug:slug>/", views.getBooksByAuthor, name="author"),
]
