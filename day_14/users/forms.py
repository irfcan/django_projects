from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = forms.widgets.TextInput(attrs={"class": "form-control"})
        self.fields["password"].widget = forms.widgets.PasswordInput(attrs={"class": "form-control"})
        
        
class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = forms.widgets.TextInput(attrs={"class": "form-control"})
        self.fields["email"].widget = forms.widgets.EmailInput(attrs={"class": "form-control"})
        self.fields["first_name"].widget = forms.widgets.TextInput(attrs={"class": "form-control"})
        self.fields["last_name"].widget = forms.widgets.TextInput(attrs={"class": "form-control"})
        self.fields["password1"].widget = forms.widgets.PasswordInput(attrs={"class": "form-control"})
        self.fields["password2"].widget = forms.widgets.PasswordInput(attrs={"class": "form-control"})
        self.fields["email"].required = True