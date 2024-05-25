from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Makale
from django.core.paginator import Paginator
from gazeteapp.forms import MakaleForm

# Create your views here.


def index(request):
    makaleler = Makale.objects.filter(activate=True)
    yazarlar = Author.objects.all()
    
    paginator = Paginator(makaleler, 3)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, "gazeteapp/index.html", {
        "page_obj": page_obj,
        "authors": yazarlar
    })

def makale_details(request, slug):
    makale = get_object_or_404(Makale, slug=slug)
    
    context = {
        "article": makale
    }
    
    return render(request, "gazeteapp/makale-details.html", context)


def makale_create(request):
    if request.method == "POST":
        form = MakaleForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = MakaleForm()
        
    return render(request, "gazeteapp/makale-create.html", {"form": form})

def makale_list(request):
    makaleler = Makale.objects.all()
    
    return render(request, "gazeteapp/makale-list.html", {"articles": makaleler})

def makale_edit(request, slug):
    makale = get_object_or_404(Makale, slug=slug)
    
    if request.method == "POST":
        form = MakaleForm(request.POST, request.FILES, instance=makale)
        form.save()
        return redirect("makale-list")
    else:
        form = MakaleForm(instance=makale)
        
    return render(request, "gazeteapp/makale-edit.html", {"form": form})


def makale_delete(request, slug):
    makale = get_object_or_404(Makale, slug=slug)
    
    if request.method == "POST":
        makale.delete()
        return redirect("makale-list")
    
    return render(request, "gazeteapp/makale-delete.html", {"article": makale})


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


def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        makaleler = Makale.objects.filter(title__icontains=q, activate=1).order_by("created_date")
        yazarlar = Author.objects.all()
        
    else:
        return redirect("index")
    
    return render(request, "gazeteapp/search.html", {
        "articles": makaleler,
        "authors": yazarlar
    })