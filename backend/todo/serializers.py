# todo/serializers.py

from rest_framework import serializers
from .models import Todo, Document
from backend import settings

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')

class DocumentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Document
        fields = ('docfile', )
