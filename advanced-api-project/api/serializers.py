from rest_framework import serializers
from .models import Author, Book
from django.db import models
import datetime

# Serializes the Book model and its fields for API representation and validation
class BookSerializer(serializers.ModelSerializer):
    class Meta():
        model = Book # Specifies the model to serialize.
        fields = ['title', 'publication_year', 'author'] # Fields to include in the output.
        
    # Validates that the publication year is not in the future.
    def validate(self, data):
        current_year = datetime.datetime.now().year
        if data['publication_year'] > current_year:
            raise serializers.ValidationError('Publication year cannot be in the future.')
        return data
            
# Serializes the Author model and its fields, including the related books.
class AuthorSerializer(serializers.ModelSerializer):
    
    # Serializes related books using BookSerializer.
    # many=True: One author can have multiple books.
    books = BookSerializer(many=True, read_only=True)
    class Meta():
        model = Author # Specifies the model to serialize.
        fields = ['name', 'books'] # Fields to include in the output. 
        
