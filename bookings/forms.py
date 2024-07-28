from django import forms
from .models import Book

#Creates a form based on the model.
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('date', 'amount', 'session_type', 'options', 'wishes')