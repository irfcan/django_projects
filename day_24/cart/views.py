from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse

from store.models import Product, Category
from .cart import Cart

# Create your views here.

class CartSummaryView(TemplateView):
    template_name = "cart/cart-summary.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        context["categories"] = Category.objects.all()
        return context
    
class CartAddView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        
        if request.POST.get("action") == "post":
            product_id = int(request.POST.get('product_id'))
            product_quantity = int(request.POST.get("product_quantity"))
            
            product = get_object_or_404(Product, id=product_id)
            
            cart.add(product=product, product_qty=product_quantity)
            
            cart_quantity = len(cart)
            
            return JsonResponse({"qty": cart_quantity})
        
        return JsonResponse({"error": "Invalid request"})


class CartDeleteView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        
        if request.POST.get("action") == "post":
            product_id = int(request.POST.get('product_id'))
            
            cart.delete(product=product_id)
            
            cart_quantity = len(cart)
            cart_total = cart.get_total()
            
            return JsonResponse({"qty": cart_quantity, "total": cart_total})

        return JsonResponse({"error": "Invalid request"})
    
class CartUpdateView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        
        if request.POST.get("action") == "post":
            product_id = int(request.POST.get('product_id'))    
            product_quantity = int(request.POST.get("product_quantity"))

            cart.update(product=product_id, qty=product_quantity)
            
            cart_quantity = len(cart)
            cart_total = cart.get_total()
            
            return JsonResponse({"qty": cart_quantity, "total": cart_total})

        return JsonResponse({"error": "Invalid request"})