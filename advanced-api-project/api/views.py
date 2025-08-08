from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# This view handles listing all books(GET).
# GET: Allows all users to access the books.
# Uses IsAuthenticatedOrReadOnly to enforce permissions.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
# This view handles creating a new book(POST).
# POST: Restricted to authenticated users only.
# Uses IsAuthenticatedOrReadOnly to enforce permissions
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
# This view handles listing a single book(GET).
# GET: Accessible to all users
# Uses IsAuthenticatedOrReadOnly to enforce permissions.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
# This view handles updating(PUT/PATCH).
# PUT/PATCH: Accessible to authenticated users only
# Uses IsAuthenticatedOrReadOnly to enforce permissions.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
# This view handles deleting(DELETE).
# DELETE: Accessible to authenticated users only
# Uses IsAuthenticatedOrReadOnly to enforce permissions.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    