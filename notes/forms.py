from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    """
    Form for creating and updating notes.
    """
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter note title', 'class':'my=5, form-control'},),
            'content': forms.Textarea(attrs={'placeholder': 'Enter note content', 'class':'my-5 form-control', 'rows': 5}),
        }
        labels = {
            'title': 'Note Title',
            'content': 'Note Content',
        }
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'Django' not in title:
            raise forms.ValidationError("Title must contain the word 'Django'.")
        return title