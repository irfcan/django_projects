from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Category, Book
from django.core.paginator import Paginator

# Create your views here.

data = {
    "tarih": "Tarih kategorisindeki kitap listesi",
    "roman": "Roman kategorisindeki kitap listesi",
    "psikoloji": "Psikoloji kategorisindeki kitap listesi",
    "Macera": "Macera kategorisindeki kitap listesi",
    "Hikaye": "Hikaye kategorisindeki kitap listesi",
}



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

def getBooksByCategory(request, slug):
    kitaplar = Book.objects.filter(category__slug=slug, activate=1)
    kategoriler = Category.objects.all()
    
    paginator = Paginator(kitaplar, 2)
    page = request.GET.get('page', 1)
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