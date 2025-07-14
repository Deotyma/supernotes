from django.contrib import admin

# Register your models here.
from . models import Note

class NoteAdmin(admin.ModelAdmin):
    """
    Admin interface for managing notes.
    """
    list_display = ('pk','title', 'created_at', 'updated_at','likes')
    search_fields = ('title', 'content')
    ordering = ('-created_at','likes')

admin.site.register(Note, NoteAdmin)