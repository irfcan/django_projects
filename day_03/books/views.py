from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("anasayfa")

def books(request):
    return HttpResponse("Kitaplar Sayfası")

def getBooksByCategory(request):
    return HttpResponse("Kategoriye göre kitap listesi")

def getBooksByAuthor(request):
    return HttpResponse("Yazara göre kitap listesi")

def authors(request):
    return HttpResponse("Yazarlar Sayfası")

def categories(request):
    return HttpResponse("Kategoriler Sayfası")


def bookdetail(request, id):
    return HttpResponse(f"{id} Numaralı Kitap Detay Sayfası")

def bookdetailname(request, name):
    liste = name.split("-")
    name = ""
    new = [i.title() for i in liste]
    for n in new:
        name += n + " "
    return HttpResponse(f"{name} Adlı Kitap Detay Sayfası")
