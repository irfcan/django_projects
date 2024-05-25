from django.shortcuts import render
from books.models import Category
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request, "pages/index.html", {"categories": categories})

class IndexView(TemplateView):
    template_name = "pages/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

def contact(request):
    return render(request, "pages/contact.html")

class ContactView(TemplateView):
    template_name = "pages/contact.html"

def about(request):
    return render(request, "pages/about.html")

class AboutView(TemplateView):
    template_name = "pages/about.html"