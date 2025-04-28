# bookmodule/forms.py
from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price']
        labels = {
            'title': 'Title',
            'author': 'Author',
            'price' : 'Price',
        }
    widgets = {
        'title': forms.TextInput(attrs={'placeholder':'Enter title'}),
        'author': forms.TextInput(attrs={'placeholder':'Enter author'}),
        'price': forms.NumberInput(attrs={'step': '0.01','placeholder':'Enter price'}),

    }
