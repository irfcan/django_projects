from django.shortcuts import render
from books.models import Category

# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request, "pages/index.html", {"categories": categories})

def contact(request):
    return render(request, "pages/contact.html")

def about(request):
    return render(request, "pages/about.html")