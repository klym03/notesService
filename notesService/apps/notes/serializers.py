# notes/serializers.py
from rest_framework import serializers
from .models import Note1

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note1
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
