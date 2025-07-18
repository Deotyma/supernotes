from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView

from.models import Note
from .forms import NoteForm

def add_like_view(request, pk):
    if request.method != 'POST':
        note = get_object_or_404(Note, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse('notes.detail', args=(pk,)))
    else:
        raise Http404("Invalid request method. Only POST requests are allowed.")

class NoteDeleteView(DeleteView):
    """
    Class-based view for deleting a note.
    """
    model = Note
    template_name = 'notes/notes_delete.html'
    success_url = '/smart/notes'  # Redirect to the list of notes after deletion


class NoteUpdateView(UpdateView):
    """
    Class-based view for updating an existing note.
    """
    model = Note
    template_name = 'notes/notes_create.html'
    success_url = '/smart/notes'  # Redirect to the list of notes after update
    form_class = NoteForm  # Use the NoteForm defined in forms.py

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)

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
    
class NoteUpdateView(UpdateView):

    model = Note
    template_name = 'notes/notes_create.html'
    pk_url_kwarg = 'pk'  # The primary key of the note to update
    success_url = '/smart/notes'  # Redirect to the list of notes after update
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