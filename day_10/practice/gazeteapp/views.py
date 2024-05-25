from django.shortcuts import render, get_object_or_404
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

def makale_details(request, slug):
    makale = get_object_or_404(Makale, slug=slug)
    
    context = {
        "article": makale
    }
    
    return render(request, "gazeteapp/makale-details.html", context)



def about(request):
    return render(request, "gazeteapp/about.html")

def authors(request):
    yazarlar = Author.objects.all()
        
    return render(request, "gazeteapp/authors.html", {"authors": yazarlar})

def author_details(request, slug):
    author = get_object_or_404(Author, slug=slug)
    context = {
        "author": author
    }
    
    return render(request, "gazeteapp/author-details.html", context)

def getMakaleByAuthors(request, slug):
    makaleler = Makale.objects.filter(author__slug=slug, activate=1) # yazara göre makale göstermek için backend bilgisi
    yazarlar = Author.objects.all() # yan menü için gerekli backend bilgisi
    
    context = {
        "articles": makaleler,
        "authors": yazarlar
    }
    
    return render(request, "gazeteapp/list.html", context)