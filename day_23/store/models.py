from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, db_index=True)
    
    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"
        
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name="product", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, default="markasız")
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="images/")
    
    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
        ordering = ["id"]
        
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
    
    

        
    
    
