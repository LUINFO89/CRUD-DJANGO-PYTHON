from dataclasses import field
from django import forms

from .models import Libros

class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields =  '__all__'
