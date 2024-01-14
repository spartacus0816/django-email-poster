from .models import Client
from django import forms

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'username', 'phone_number', 'email']
        

class ClienThankyouForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField()
    