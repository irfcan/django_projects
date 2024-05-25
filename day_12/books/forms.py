from django import forms
from .models import Book, Category, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['name', 'author', 'category', 'description', 'stock', 'price', 'publication_date', 'activate']
        
        labels = {
            "name": "Kitap Adı",
            "author": "Yazar Adı",
            "category": "Kategori",
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
                "required": "Yazar adı girmelisiniz"
            },
            "category": {
                "required": "Kategori adı girmelisiniz"
            }
        }


        
                
class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("name", "biography")
        labels = {
            "name": "Yazar Adı",
            "biography": "Biyografi"
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "biography": forms.Textarea(attrs={"class": "form-control"}),
        }
    
    
    

# class BookCreateForm(forms.Form):
#     name = forms.CharField(label="Kitap Adı",
#                            required=True,
#                            error_messages={"required": "Kitap adı girmelisiniz"},
#                            widget=forms.TextInput(attrs={"class": "form-control"}))
#     author = forms.CharField(label="Yazar Adı",
#                              required=True,
#                              error_messages={"required": "Yazar adı girmelisiniz"},
#                              widget=forms.TextInput(attrs={"class": "form-control"}))
#     category = forms.CharField(label="Kategori Adı",
#                              required=True,
#                              error_messages={"required": "Kategori adı girmelisiniz"},
#                              widget=forms.TextInput(attrs={"class": "form-control"}))
#     description = forms.CharField(required=False,
#                                   widget=forms.Textarea(attrs={"class": "form-control"}))
#     stock = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
#     price = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
#     publication_date = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
#     activate = forms.BooleanField()