from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Makale

# Create your views here.


def index(request):
    makaleler = Makale.objects.all()
    print(makaleler)
    print(type(makaleler))
    makale = ""
    for i in makaleler:
        makale += str(i) + " "
        
    return HttpResponse(makale)

def about(request):
    return render(request, "about.html")

def authors(request):
    yazarlar = Author.objects.all()
    yazar = ""
    for i in yazarlar:
        yazar += str(i) + " "
        
    return render(request, "authors.html", {"author": yazar})