from .models import Book
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('date', 'amount', 'session_type', 'options', 'wishes')