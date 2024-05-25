from django import forms

class BookCreateForm(forms.Form):
    name = forms.CharField()
    author = forms.CharField()
    category = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    stock = forms.IntegerField()
    price = forms.IntegerField()
    publication_date = forms.IntegerField()
    activate = forms.BooleanField()