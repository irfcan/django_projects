from django.shortcuts import render, get_object_or_404
from store.models import Category, Product
from django.views import View
from django.views.generic import ListView, DetailView

# Create your views here.

#class
class StoreView(View):
    template_name = "store/store.html"
    
    def get(self, request, *args, **kwargs):
        all_products = Product.objects.all()
        context = {"products": all_products}
        return render(request, self.template_name, context)
    
# generic class
class StoreGenericView(ListView):
    model = Product
    template_name = "store/store.html"
    context_object_name = "products"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    
#class
class CategoriesView(View):
    template_name = "store/categories.html"
    
    def get(self, request, *args, **kwargs):
        all_categories = Category.objects.all()
        context = {"all_categories": all_categories}
        return render(request, self.template_name, context)
    
#generic
class CategoriesGenericView(ListView):
    model = Category
    template_name = "store/categories.html"
    context_object_name = "all_categories"
    
    
#class
class ListCategoryView(View):
    template_name = "store/list-category.html"
    
    def get(self, request, category_slug=None, *args, **kwargs):
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        context = {"category": category, "products": products}
        return render(request,self.template_name, context)
    
#generic

class ListCategoryGenericView(DetailView):
    model = Category 
    template_name = "store/list-category.html"
    context_object_name = "category"
    slug_url_kwarg = "category_slug"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category=self.object) # category eşittir daha önce sorgulanmış categori nesnesini buraya yazmamız gerekiyor bu nedenle self.object yazılması gerekiyor.
        return context
    
    

# def list_category(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     products = Product.objects.filter(category=category)
#     context = {
#         "category": category,
#         "products": products
#     }
    
#     return render(request, "store/list-category.html", context)

#class
class ProductInfoView(View):
    template_name = "store/product-info.html"
    
    def get(self, request, product_slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=product_slug)
        context = {"product": product}
        return render(request, self.template_name, context)
    
    
#generic

class ProductInfoGenericView(DetailView):
    model = Product
    template_name = "store/product-info.html"
    context_object_name = "product"
    slug_url_kwarg = "product_slug"