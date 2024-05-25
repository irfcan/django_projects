from django.shortcuts import render
from phoneBook.models import Category, Phone
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

# Create your views here.


class IndexView(ListView):
    model = Phone
    template_name = "phoneBook/index.html"
    context_object_name = "phones"
    queryset = Phone.objects.filter(activate=1, isHome=1)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context