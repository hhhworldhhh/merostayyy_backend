from django.forms import ModelForm
from .models import hotel_info
from crispy_forms.layout import Field
from django import forms
class Hotel_info_Form(ModelForm):
    
    class Meta:
        model=hotel_info
        exclude = ['slug']

    