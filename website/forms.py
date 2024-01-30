from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email= forms.EmailField(label="",widget=forms.TextInput(attr={'class':'form-control','placeholder':'Email'}))
    firstname= forms.CharField(label="",max_legth="100", widget=forms.TextInput(attr={'class':'form-control','placeholder':'Firstname'}))
    lastname= forms.CharField(label="",max_legth="100", widget=forms.TextInput(attr={'class':'form-control','placeholder':'Lastname'}))

class Meta:
    model = User
    fields = ['username','email', 'firstname', 'lastname', 'password1', 'password2']







