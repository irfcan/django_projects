from django.contrib import admin
from .models import Author, Category, Book

# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
