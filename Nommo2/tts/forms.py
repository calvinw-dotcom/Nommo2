from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import RequestMp3


#Registering a new user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


#login existing user
class LogInForm (AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


#URL to convert

class UrlRequestForm (forms.ModelForm):
    class Meta:
        model=RequestMp3
        fields = ['requested_url']