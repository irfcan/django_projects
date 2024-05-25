from django.db import models
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, default=None)
    image = models.ImageField(upload_to="image", default="")
    biography = models.TextField(max_length=1000, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Yazar"
        verbose_name_plural = "Yazarlar"
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, default=None)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, related_name="book")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image", default="")
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, default=None, editable=False, db_index=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    stock = models.IntegerField()
    price = models.FloatField()
    publication_date = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Kitap"
        verbose_name_plural = "Kitaplar"
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    