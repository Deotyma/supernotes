from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView

from.models import Note
from .forms import NoteForm

class NoteCreateView(CreateView):
    """
    Class-based view for creating a new note.
    """
    model = Note
    template_name = 'notes/notes_create.html'
    success_url = '/smart/notes'  # Redirect to the list of notes after creation
    form_class = NoteForm  # Use the NoteForm defined in forms.py

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)

class NoteListView(ListView):
    """
    Class-based view for rendering a list of notes.
    """
    model = Note
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'

class PopularNoteListView(ListView):
    
    model = Note
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'
    queryset = Note.objects.filter(likes__gte=1).order_by('-likes')

class NoteDetailView(DetailView):
    """
    Class-based view for rendering the details of a specific note.
    """
    model = Note
    template_name = 'notes/notes_detail.html'
    context_object_name = 'note'

""" def notes_detail(request, pk):
   
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return render(request, 'notes/404.html', status=404)
    
    return render(request, 'notes/notes_detail.html', {
        'note': note
    })
 """