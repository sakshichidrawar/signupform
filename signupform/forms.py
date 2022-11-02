from django import forms
from django.core import validators 

class signform(forms.Form):
    password=forms.CharField(widget=forms.PasswordInput) 
    rpassword=forms.CharField(label='Password(again)',widget=forms.PasswordInput) 

    def clean(self): 
        cleaned_data=super().clean()
        pwd=cleaned_data['password'] 
        rpwd=cleaned_data['rpassword'] 
        if pwd!=rpwd:   
            raise forms.ValidationError('Both Passwords must be same')