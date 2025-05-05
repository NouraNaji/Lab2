# bookmodule/forms.py
from django import forms
from .models import Book, Student, Address
from .models import  Student2, Address2
from .models import BookCover


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price']
        labels = {
            'title': 'Title',
            'author': 'Author',
            'price': 'Price',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Enter author'}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Enter price'}),
        }

# lab11
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']

class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['street', 'city']

class Student2Form(forms.ModelForm):
    addresses = forms.ModelMultipleChoiceField(
        queryset=Address2.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']


class BookCoverForm(forms.ModelForm):
    class Meta:
        model = BookCover
        fields = ['title', 'description', 'image']