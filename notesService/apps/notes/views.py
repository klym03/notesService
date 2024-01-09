from django.shortcuts import render

# Create your views here.
# notes/views.py
from rest_framework import generics
from .apps import NotesConfig
from .models import Note1
from .serializers import NoteSerializer


class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note1.objects.all()
    serializer_class = NoteSerializer

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note1.objects.all()
    serializer_class = NoteSerializer
