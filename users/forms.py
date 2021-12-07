from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import New_user

class New_userForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    contact_number = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta:
        model = New_user
        fields = ['first_name', 'last_name', 'username', 'email', 'contact_number', 'password1', 'password2']