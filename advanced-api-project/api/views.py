from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import render
from rest_framework import generics, filters, fields
from .models import Book
from .serializers import BookSerializer

# This view handles listing all books(GET).

# GET: Allows all users to access the books.

# Uses IsAuthenticatedOrReadOnly to enforce permissions.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Enables filtering, searching and ordering in API requests.
    
    # SearchFilter: allows the search keyword on specified fields.
    
    #OrderingFilter: allows sorting results by specified fields.
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # Field users can search bu using ?search=keyword
    
    search_fields = ['title', 'publication_year', 'author'] 
    
    # Field users can order by using ?ordering=field or ?ordering=-field
    
    ordering_fields = ['title', 'publication_year']
    
# This view handles creating a new book(POST).

# POST: Restricted to authenticated users only.

# Uses IsAuthenticatedOrReadOnly to enforce permissions

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
# This view handles listing a single book(GET).

# GET: Accessible to all users.

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
    