from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from cart.cart import Cart
from store.models import Product
from django.http import JsonResponse

class CartSummaryView(TemplateView):
    template_name = "cart/cart-summary.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        return context


class CartAddView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        
        if request.POST.get('action') == "POST":
            product_id = int(request.POST.get("product_id"))
            product_quantity = int(request.POST.get("product_quantity"))
            
            product = get_object_or_404(Product, id=product_id)
            
            cart.add(product=product, product_qty=product_quantity)
            
            cart_quantity = len(cart)
            
            return JsonResponse({"qty": cart_quantity})
        
        return JsonResponse({"error": "Invalid request"})

