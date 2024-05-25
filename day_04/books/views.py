from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Category, Book

# Create your views here.

data = {
    "tarih": "Tarih kategorisindeki kitap listesi",
    "roman": "Roman kategorisindeki kitap listesi",
    "psikoloji": "Psikoloji kategorisindeki kitap listesi",
}

def index(request):
    return HttpResponse("anasayfa")

def books(request):
    return HttpResponse("Kitaplar Sayfası")

def getBooksByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
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

def getBooksByAuthor(request):
    return HttpResponse("Yazara göre kitap listesi")

def authors(request):
    return HttpResponse("Yazarlar Sayfası")

def categories(request):
    return HttpResponse("Kategoriler Sayfası")


def bookdetail(request, id):
    try:
        book = Book.objects.get(id=id)
        return HttpResponse(f"{book} Kitabının Detay Sayfası")
    except Book.DoesNotExist:
        return HttpResponseNotFound("Kitap Bulunamadı")
    
def bookdetailname(request, slug_name):
    try:
        book = Book.objects.get(slug=slug_name)
        return HttpResponse(f"{book} Adlı Kitap Detay Sayfası")
    except Book.DoesNotExist:
        return HttpResponseNotFound("Kitap Bulunamadı")