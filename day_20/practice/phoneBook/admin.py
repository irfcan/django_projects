from django.contrib import admin
from phoneBook.models import Category, Phone

# Register your models here.


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("ad", "soyad", "telefon", "sehir", "slug", "activate", "isHome", "category_list")
    list_display_links = ("ad", "soyad", "slug")
    readonly_fields = ("slug",)
    list_filter = ("activate", "isHome")
    list_editable = ("activate", "isHome")
    search_fields = ("ad", "soyad")
    
    def category_list(self, obj):
        html = ""
        for category in obj.kategori.all():
            html += category.name + " "
            
        return html
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_display_links = ("slug",)
    readonly_fields = ("slug",)
    search_fields = ("name",)