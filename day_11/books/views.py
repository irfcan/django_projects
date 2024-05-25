from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Category, Book
from django.core.paginator import Paginator
from .forms import BookCreateForm

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


# def create_book(request):
#     if request.method == "POST":
#         name = request.POST["name"]
#         author = request.POST["author"]
#         category = request.POST["category"]
#         description = request.POST["description"]
#         stock = request.POST["stock"]
#         price = request.POST["price"]
#         publication_date = request.POST["publication_date"]
#         activate = request.POST.get("activate", False)
        
#         if activate == "on":
#             activate = True
        
#         author, created = Author.objects.get_or_create(name=author)    # (yazar, true)
#         category, created = Category.objects.get_or_create(name=category) # (category, true)
            
#         book = Book.objects.create(name=name, category=category, description=description,
#                     stock=stock, price=price, publication_date=publication_date, activate=activate)
        
#         book.author.add(author)
        
#         return redirect("/books")
        
#     return render(request, "books/book-create.html")


def create_book(request):
    if request.method == "POST":
        form = BookCreateForm(request.POST)
        
        if form.is_valid():
            category, created = Category.objects.get_or_create(name=form.cleaned_data["category"]) # (category, true)
            book = Book.objects.create(
                name = form.cleaned_data["name"],
                category = category,
                description = form.cleaned_data["description"],
                stock = form.cleaned_data["stock"],
                price = form.cleaned_data["price"],
                publication_date = form.cleaned_data["publication_date"],
                activate = form.cleaned_data["activate"],
            )
            
            author, created = Author.objects.get_or_create(name=form.cleaned_data["author"])    # (yazar, true)            category, created = Category.objects.get_or_create(name=form.cleaned_data["category"]) # (category, true)
        
            
            book.author.add(author)
            
            return redirect("/books")
    else:    
        form = BookCreateForm()
        
        
    return render(request, "books/book-create.html", {"form": form})

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