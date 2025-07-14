from django.db import models

# Create your models here.
class Note(models.Model):
    """
    Model representing a note in the SmartNotes application.
    """
    title = models.CharField(max_length=200, help_text='Enter the title of the note')
    content = models.TextField(help_text='Enter the content of the note')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Date and time when the note was created')
    updated_at = models.DateTimeField(auto_now=True, help_text='Date and time when the note was last updated')
    likes = models.PositiveIntegerField(default=0, help_text='Number of likes for the note')