from django import forms
from django.forms import ModelForm
from .models import listings

class CreateListingsForm(forms.ModelForm): 
    class Meta: 
        model = listings 
        fields = ['title', 'description', 'price', 'image'] 