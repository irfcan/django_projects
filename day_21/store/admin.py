from django.contrib import admin
from store.models import Category, Product

# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "brand", "slug")
    list_display_links = ("title", "slug")
    prepopulated_fields = {"slug":  ("title",)}
