from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    """
    Form for creating and updating notes.
    """
    class Meta:
        model = Note
        fields = ['title', 'content']
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'Django' not in title:
            raise forms.ValidationError("Title must contain the word 'Django'.")
        return title