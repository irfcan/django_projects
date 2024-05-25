from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Makale

# Create your views here.


def index(request):
    makaleler = Makale.objects.filter(activate=True)
    yazarlar = Author.objects.all()

    return render(request, "gazeteapp/index.html", {
        "articles": makaleler,
        "authors": yazarlar
    })

def about(request):
    return render(request, "gazeteapp/about.html")

def authors(request):
    yazarlar = Author.objects.all()
        
    return render(request, "gazeteapp/authors.html", {"authors": yazarlar})