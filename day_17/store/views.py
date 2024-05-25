from django.shortcuts import render
from store.models import Category, Product
from django.views import View
from django.views.generic import ListView, DetailView

# Create your views here.

class StoreView(View):
    template_name = "store/store.html"
    
    def get(self, request, *args, **kwargs):
        all_products = Product.objects.all()
        context = {"my_products": all_products}
        return render(request, self.template_name, context)