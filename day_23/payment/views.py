from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse

from payment.models import ShippingAddress, Order, OrderItem
from cart.cart import Cart
from payment.forms import ShippingForm

class CheckoutView(TemplateView):
    
    template_name = "payment/checkout.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        
        # Eğer kullanıcı oturum açmışsa, gönderi bilgilerini kontrol et
        if self.request.user.is_authenticated:
            try:
                shipping_address = ShippingAddress.objects.get(user=self.request.user.id)
                
                context["shipping"] = shipping_address
                
            except ShippingAddress.DoesNotExist:
                pass
            
        return context


class CompleteOrderView(View):
    def post(self, request, *args, **kwargs):
        if request.POST.get("action") == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            address1 = request.POST.get("address1")
            address2 = request.POST.get("address2")
            city = request.POST.get("city")
            state = request.POST.get("state")
            zipcode = request.POST.get("zipcode")
            
            shipping_address = f"{address1}\n{address2}\n{city}\n{state}\n{zipcode}"
            
            cart = Cart(request)
            
            total_cost = cart.get_total()
            
            if request.user.is_authenticated:
                order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address, 
                                             amount_paid=total_cost, user=request.user)
                
                order_id = order.pk
                
                for item in cart:
                    OrderItem.objects.create(order_id=order_id, product=item["product"],
                                             quantity=item["qty"], price=item["price"],
                                             user=request.user)
                    
            else:
                order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address, 
                                             amount_paid=total_cost, user=request.user)
                
                order_id = order.pk
                
                for item in cart:
                    OrderItem.objects.create(order_id=order_id, product=item["product"],
                                             quantity=item["qty"], price=item["price"],
                                             user=request.user)
                    
            order_success = True
            return JsonResponse({"success": order_success})
        
        
        return JsonResponse({"success": False, "error": "Invalid request"})
    
class PaymentSuccessView(TemplateView):
    template_name = "payment/payment-success.html"
    
    def post(self, request, *args, **kwargs):
        #sepeti temizle
        
        for key in list(request.session.keys()):
            if key == "session_key":
                del request.session[key]
                
        return render(request, self.template_name)
   
   
class PaymentFailedView(TemplateView) :
    template_name = "payment/payment-failed.html"