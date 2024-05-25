from django import forms
from gazeteapp.models import Makale, Author

class MakaleForm(forms.ModelForm):
    class Meta:
        model = Makale
        fields = ["title", "author", "image", "content", "activate", "isHome"] 
        labels = {
            "title": "Makale Adı",
            "author": "Yazar Adı",
            "image": "Resim Yükle",
            "content": "İçerik",
            "activate": "Aktiflik",
            "isHome": "Anasafada Görünsün"
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }
        error_messages = {
            "title": {
                "required": "Kitap başlığı girmelisiniz",
                "max_length": "Maksimum 100 karakter girmelisiniz"
            },
            "author": {
                "required": "Yazar adı girmelisiniz",
                "max_length": "Maksimum 100 karakter girmelisiniz"
            }
        }