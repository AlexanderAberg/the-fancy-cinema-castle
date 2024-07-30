from django import forms
from .models import Book

#Creates a form based on the model.
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('date', 'amount', 'session_type', 'wishes')

  #  def __init__(self, *args, **kwargs):
   #     super().__init__(*args, **kwargs)
        
    #    self.fields['options'] = forms.MultipleChoiceField()