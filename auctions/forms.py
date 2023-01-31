from django import forms
from django.forms import ModelForm
from .models import listings, bids

class CreateListingsForm(forms.ModelForm): 
    class Meta: 
        model = listings 
        fields = ['title', 'description', 'category', 'price', 'image'] 

class BidsForm(forms.ModelForm): 
    class Meta: 
        model = bids 
        fields = ['bids'] 