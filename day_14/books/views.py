from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Category, Book
from django.core.paginator import Paginator
from .forms import BookForm, AuthorCreateForm

# Create your views here.

def index(request):
    books = Book.objects.filter(activate=1)
    categories = Category.objects.all()
    
    paginator = Paginator(books, 2)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    
    context = {
        "page_obj": page_obj,
        "categories": categories,
    }
    return render(request, "books/index.html", context)


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect("/books")
    else:    
        form = BookForm()
        
        
    return render(request, "books/book-create.html", {"form": form})


def book_list(request):
    kitaplar = Book.objects.all()
    
    context = {
        "books": kitaplar
    }
    
    return render(request, "books/book-list.html", context)

def book_edit(request, slug):
    book = get_object_or_404(Book, slug=slug)
    
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        form.save()
        return redirect("book-list")
    else:
        form = BookForm(instance=book)
        
    return render(request, "books/book-edit.html", {"form": form})
    
    
def book_delete(request, slug):
    book = get_object_or_404(Book, slug=slug)
    
    if request.method == "POST":
        book.delete()
        return redirect("book-list")
    
    return render(request, "books/book-delete.html", {"book":book})

def author_create(request):
    if request.method == "POST":
        form = AuthorCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect("/books")
    
    else:
        form = AuthorCreateForm()
        
    return render(request, "books/author-create.html", {"form": form})

def getBooksByCategory(request, slug):
    kitaplar = Book.objects.filter(category__slug=slug, activate=1)
    kategoriler = Category.objects.all()
    
    # Sayfa başına 2 kitapla bir Paginator oluştur
    paginator = Paginator(kitaplar, 2)
    
    # İstekten gelen GET parametrelerinde belirtilen sayfa numarasını al, 
    # belirtilmemişse 1 olarak varsay
    page = request.GET.get('page', 1)
    
    # İstenen sayfa için Page objesini al
    page_obj = paginator.get_page(page)
    
    context = {
        "page_obj": page_obj,
        "categories": kategoriler,
        "seciliKategori": slug,
    }
    
    return render(request, "books/index.html", context)


def getBooksByAuthor(request, slug):
    author = Author.objects.get(slug=slug)
    return HttpResponse(f"{author} adlı yazara ait kitaplar")

def authors(request):
    authors = Author.objects.all()
    context = {"authors": authors}
    return render(request, "books/authors.html", context)

def categories(request):
    return render(request, "books/categories.html", {"categories": Category.objects.all()})


def bookdetail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    context = {
        "kitap": book
    }
    
    return render(request, "books/book-detail.html", context)
    
def bookdetailname(request, slug_name):
    try:
        context = {"book" : Book.objects.get(slug=slug_name)}
        return render(request, "books/book-detail-name.html", context)
    except Book.DoesNotExist:
        return HttpResponseNotFound("Kitap Bulunamadı")
    
    
def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kitaplar = Book.objects.filter(activate=1, name__icontains=q).order_by("created_date")
        kategoriler = Category.objects.all()
    else:
        return redirect("/books")
    
    paginator = Paginator(kitaplar, 2)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    
    context = {
        "page_obj": page_obj,
        "categories": kategoriler,
    }
    
    return render(request, "books/list.html", context)


def upload(request):
    if request.method == "POST" and request.FILES:
        uploaded_image = request.FILES["image"]
        handle_uploaded_file(uploaded_image)
        return render(request, "books/success.html")
    return render(request, "books/upload.html")

import random
import os

def handle_uploaded_file(file):
    number = random.randint(1, 99999)
    filename, file_extention = os.path.splitext(file.name) # buradan (dosya ismi, dosya_adı) şeklinde bir tuple sonucu çıkar
    name = filename + "_" + str(number) + file_extention
    
    with open("temp/" + name, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)