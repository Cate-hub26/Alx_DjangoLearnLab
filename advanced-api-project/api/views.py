from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# This view handles listingall books(GET) and creating a new book(POST).
# GET: Allows all users to access the books.
# POST: Restricted to authenticated users only.
# Uses IsAuthenticatedOrReadOnly to enforce permissions.
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
# This view handles listing a single book(GET), updating(PUT/PATCH) and deleting(DELETE).
# GET: Accessible to all users
# PUT/PATCH/DELETE: Accessible to authenticated users only
# Uses IsAuthenticatedOrReadOnly to enforce permissions.
class BookDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
