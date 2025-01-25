# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
                "id": "password-field"
            }
        ))


# class SignUpForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Username",
#                 "class": "form-control"
#             }
#         ))
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "placeholder": "Email",
#                 "class": "form-control"
#             }
#         ))
#     first_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Your First Name",
#                 "class": "box-input" ,
#                 "name":'first_name',
#             }
#         ))
   
  
   
#     # Country = forms.CharField(
#     #     widget=forms.TextInput(
#     #         attrs={
#     #             "placeholder": "country",
#     #             "class": "form-control"
#     #         }
#     #     ))
    
    
    
      
      

#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Password",
#                 "class": "form-control",
#                 "id": "password-field"

#             }
#         ))
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Password check",
#                 "class": "form-control",
#                 "id": "password-field2"
#             }
#         ))

#     referral_code= forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Referal",
#                 'value': 'site name',
#                 "class": "form-control",
#                 "id": "refid",
                
#                 "readonly": True,
           
#             }
#         ))

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2',
#                   'referral_code')


#     def clean_email(self):

#         email = self.cleaned_data.get("email")


#         if User.objects.filter(email=email).exists():

#             raise forms.ValidationError("Email in use")
#         return email
    








