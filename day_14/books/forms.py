from django import forms
from .models import Book, Category, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['name', 'author', 'category', 'image', 'description', 'stock', 'price', 'publication_date', 'activate']
        
        labels = {
            "name": "Kitap Adı",
            "author": "Yazar Adı",
            "category": "Kategori",
            "image": "Resim Yükle",
            "description": "Açıklama",
            "stock": "Stok Adeti",
            "price": "Fiyat",
            "publication_date": "Basım Yılı",
            "activate": "Aktiflik",
            "isHome": "Anasayfada Görünsün"
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.SelectMultiple(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "publication_date": forms.NumberInput(attrs={"class": "form-control"}),
        }
        error_message = {
            "name": {
                "required": "Kitap adı girmelisiniz",
                "max_length": "Maksimum 100 karakter girmelisiniz"
            },
            "author": {
                "required": "Yazar adı girmelisiniz",
                "max_length": "Maksimum 100 karakter girmelisiniz"
            },
            "category": {
                "required": "Kategori adı girmelisiniz",
                "max_length": "Maksimum 100 karakter girmelisiniz"
            }
        }


        
                
class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("name", "image", "biography")
        labels = {
            "name": "Yazar Adı",
            "biography": "Biyografi",
            "image": "Resim Yükle",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "biography": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }
    
