from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name="user")
    phone_number = models.CharField(max_length=12, verbose_name="Telefon Numarası")
    address = models.TextField(max_length=1000, verbose_name="Adres")
    activate = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Kullanıcı Profili"
        verbose_name_plural = "Kullanıcı Profilleri"
        
    def __str__(self):
        return f"{self.user}"