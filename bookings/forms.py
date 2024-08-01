from django import forms
from .models import Book
from .models import Options

#Creates a form based on the model.
class BookForm(forms.ModelForm):

   options = forms.ModelMultipleChoiceField(
       queryset=Options.objects.all(),
       widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Book
        fields = ('date', 'amount', 'session_type', 'options', 'wishes')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['options'] = forms.MultipleChoiceField()