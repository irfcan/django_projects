from django.contrib import admin
from payment.models import ShippingAddress, Order, OrderItem

# Register your models here.


# admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

@admin.register(ShippingAddress)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "user")
    list_display_links = ("full_name", "email")