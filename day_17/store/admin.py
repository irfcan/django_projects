from django.contrib import admin
from store.models import Category, Product


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
    
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
    
# slug ı otamatik olarak oluştursun neye göre oluşturulması gerekiyorsa

admin.site.register(Category)
admin.site.register(Product)