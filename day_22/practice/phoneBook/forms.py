from django import forms
from phoneBook.models import Category, Phone

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ("ad", "soyad", "telefon", "email", "image", "adres", "sehir", "lokasyon", "kategori", "activate", "isHome")
        
        labels = {
            "ad": "Adı",
            "soyad": "Soyadı",
            "kategori": "Kategori Adı",
            "telefon": "Telefon",
            "email": "E-Posta",
            "image": "Resim Yükle",
            "adres": "Adres",
            "sehir": "Şehir",
            "lokasyon": "Lokasyon",
            "activate": "Aktiflik",
            "isHome": "Anasyfada Görünsün"
        }
        
        widgets = {
            "ad": forms.TextInput(attrs={"class": "form-control"}),
            "soyad": forms.TextInput(attrs={"class": "form-control"}),
            "kategori": forms.SelectMultiple(attrs={"class": "form-control"}),
            "telefon": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "adres": forms.Textarea(attrs={"class": "form-control"}),
            "sehir": forms.Select(attrs={"class": "form-control"}),
            "lokasyon": forms.TextInput(attrs={"class": "form-control"}),
        }
        
        error_messages = {
            "ad": {
                "required": "İsim girmelisiniz",
                "max_length": "maksimum 100 karakter girmelisiniz"
            },
            "soyad": {
                "required": "Soyisim girmelisiniz",
                "max_length": "maksimum 100 karakter girmelisiniz"
            },
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)
        
        labels = {
            "name": "Kategori Adı"
        }
        
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"})
        }
        
        error_messages = {
            "name": {
                "required": "İsim girmelisiniz",
                "max_length": "maksimum 100 karakter girmelisiniz"
            }
        }