from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Category, Book

# Create your views here.

data = {
    "tarih": "Tarih kategorisindeki kitap listesi",
    "roman": "Roman kategorisindeki kitap listesi",
    "psikoloji": "Psikoloji kategorisindeki kitap listesi",
    "Macera": "Macera kategorisindeki kitap listesi",
    "Hikaye": "Hikaye kategorisindeki kitap listesi",
}



def books(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    context = {
        "books": books,
        "categories": categories
    }
    return render(request, "books/index.html", context)

def getBooksByCategory(request, category_name):# category name, hangi kategori onu gösterir
    try:
        categories = Category.objects.all() # soldaki menü için var
        category_text = data[category_name] # kategorinin içeriğinden bahseder
        return render(request, "books/books.html", {
            "category": category_name,
            "categoryText": category_text,
            "categories": categories
        })
        
    except:
        return HttpResponseNotFound("Yanlış kategori seçimi, lütfen gitmek istediğiniz sayfayı kontrol ediniz")

def getBooksByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("Yanlış Kategori Seçimi")
    
    category_name = category_list[category_id-1]
    
    redirect_url = reverse("category_name", args=[category_name])
    
    return redirect(redirect_url)
    
    # redirect_text = category_list[category_id-1]
    
    # return redirect("/books/category/" + redirect_text) # books/category/<str:category_name>/

def getBooksByAuthor(request, slug):
    author = Author.objects.get(slug=slug)
    return HttpResponse(f"{author} adlı yazara ait kitaplar")

def authors(request):
    authors = Author.objects.all()
    context = {"authors": authors}
    return render(request, "books/authors.html", context)

def categories(request):
    return render(request, "books/categories.html", {"categories": Category.objects.all()})


def bookdetail(request, id):
    try:
        book = Book.objects.get(id=id)
        return render(request, "books/book-detail.html", {"kitap": book})
    except Book.DoesNotExist:
        return HttpResponseNotFound("Kitap Bulunamadı")
    
def bookdetailname(request, slug_name):
    try:
        context = {"book" : Book.objects.get(slug=slug_name)}
        return render(request, "books/book-detail-name.html", context)
    except Book.DoesNotExist:
        return HttpResponseNotFound("Kitap Bulunamadı")