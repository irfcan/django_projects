from django.db import models
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img", default="")
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    biography = models.TextField(max_length=1000, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Yazar"
        verbose_name_plural = "Yazarlar"

class Makale(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img", default="")
    content = models.TextField(max_length=1000, blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)
    isHome = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Makale"
        verbose_name_plural = "Makaleler"
        ordering = ["id"] # veritablosu id ye göre sıralama yapsın
    
    