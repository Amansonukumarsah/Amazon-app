from cProfile import label
from dataclasses import field
from pyexpat import model
from tkinter import Widget
from wsgiref.validate import validator
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import Customer

class registrationforms(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Re_Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields=['username','email','password1','password2']
        labels= {'email':'Email'}

class loginform(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class passwordchange(PasswordChangeForm):
    old_password=forms.CharField(label='Old_password',strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(label='New_password',strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label='Confirm_password',strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))


class resetpassword(PasswordResetForm):
    email=forms.CharField(label='Email',strip=False,widget=forms.EmailInput(attrs=({'autocomplete':'Email','class':'form-control'})))

class setpassword(SetPasswordForm):
    new_password1=forms.CharField(label='New_password',strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label='Confirm_password',strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))


class Adressform(forms.ModelForm):

    class Meta:
        model = Customer
        fields=['Name','City','Pin_code','State']
        Name=forms.CharField(label='Name',widget=forms.TextInput(attrs=({'class':'form-control'})))
        City=forms.CharField(label='Name',widget=forms.TextInput(attrs=({'class':'form-control'})))
        Pin_code=forms.CharField(label='Name',widget=forms.NumberInput(attrs=({'class':'form-control'})))
        State=forms.CharField(label='Name',widget=forms.Select(attrs=({'class':'form-control'})))

