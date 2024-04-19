from django.contrib.auth.forms import UserCreationForm 
from . models import contact
from django.forms import ModelForm
from django import forms

class ContactCreationForm(forms.ModelForm):
    class Meta:
        model= contact
        fields = ('username','email','phone','text',)
