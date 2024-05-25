from django.db import models

# Create your models here.

# Veritabanında bir tablo oluşturmak için, bir sınıf oluşturun, sınıfın adı tablonun adıdır.

# Sınıfın attributes ları tablonun sütunları

# her sütuna gelecek değer satırları oluşturuyor.

class Blog(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    content = models.TextField(max_length=1000)
    date = models.DateField()
    
    def __str__(self):
        return self.title
    
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length = 100)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name