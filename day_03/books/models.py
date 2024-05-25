from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(max_length=1000, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Yazar"
        verbose_name_plural = "Yazarlar"
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True, null=True)
    stock = models.IntegerField()
    price = models.FloatField()
    publication_date = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kitap"
        verbose_name_plural = "Kitaplar"