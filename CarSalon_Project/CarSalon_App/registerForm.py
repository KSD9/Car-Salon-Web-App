from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    user_roles = (
('RentManager','Rent Manager'),
('SalesManager','Sales Manager'),
('Administrator','Administrator'),
    )
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    role = forms.ChoiceField(choices=user_roles)

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('username',  'email', 'password1', 'password2','first_name','last_name','role','image' )