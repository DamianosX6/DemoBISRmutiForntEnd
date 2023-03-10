from turtle import up
from django.forms import ModelForm
from django.db import models
from .models import   customuser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




class CreateUserForm(UserCreationForm):
    class Meta:
        model = customuser

        fields = ['username','first_name','last_name','email','password1','password2','tel','t_address','zipcode']
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({
            'size': '15',
            'class': 'form-control',
            'style': 'font-size: 12px; font-weight: bold;  margin-bottom: 20px; padding-left: 10px;',
        })
            self.fields['first_name'].widget.attrs.update({
            'size': '15',
            'class': 'form-control',
            'style': 'font-size: 12px; font-weight: bold;  margin-bottom: 20px; padding-left: 10px;',
        })
            self.fields['last_name'].widget.attrs.update({
            'size': '15',
            'class': 'form-control',
            'style': 'font-size: 12px; font-weight: bold;  margin-bottom: 20px; padding-left: 10px;',
        })
            self.fields['email'].widget.attrs.update({
            'size': '15',
            'class': 'form-control',
            'style': 'font-size: 12px; font-weight: bold;  margin-bottom: 20px; padding-left: 10px;',
        })
            self.fields['password1'].widget.attrs.update({
            'size': '15',
            'class': 'form-control',
            'style': 'font-size: 12px; font-weight: bold;  margin-bottom: 20px; padding-left: 10px;',
        })
            self.fields['password2'].widget.attrs.update({
            'size': '15',
            'class': 'form-control',
            'style': 'font-size: 12px; font-weight: bold;  margin-bottom: 20px; padding-left: 10px;',
        })
            self.fields['tel'].widget.attrs.update({
            'size': '15',
            'class': 'form-control',
            'style': 'font-size: 12px; font-weight: bold;  margin-bottom: 20px; padding-left: 10px;',
        })
            self.fields['t_address'].widget.attrs.update({
            'size': '15',
            'class': 'form-control',
            'style': 'font-size: 12px; font-weight: bold;  margin-bottom: 20px; padding-left: 10px;',
        })
            self.fields['zipcode'].widget.attrs.update({
            'size': '15',
            'class': 'form-control',
            'style': 'font-size: 12px; font-weight: bold;  margin-bottom: 20px; padding-left: 10px;',
        })