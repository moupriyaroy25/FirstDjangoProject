from django import forms

from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'title','author','add_date']
        widgets ={
            'isbn' : forms.NumberInput(attrs={'class':'form-control'}),
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'add_date' : forms.DateInput(attrs={'class':'form-control'}),
        }