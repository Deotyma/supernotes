from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NoteListView.as_view(), name='notes.list'),
    path('notes/popular/', views.PopularNoteListView.as_view()),
    path('notes/<int:pk>/', views.NoteDetailView.as_view(), name='notes.detail'),
    path('notes/<int:pk>/edit', views.NoteUpdateView.as_view(), name='notes.edit'),
    path('notes/<int:pk>/delete', views.NoteDeleteView.as_view(), name='notes.delete'),
    path('notes/create/', views.NoteCreateView.as_view(), name='notes.create'),
    path('notes/<int:pk>', views.add_like_view, name='notes.add_like'),
]