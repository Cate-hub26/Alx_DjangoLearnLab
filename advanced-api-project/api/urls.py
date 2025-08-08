from django.urls import path
from .views import (BookListView, BookCreateView, 
BookDetailView, BookUpdateView, BookDeleteView)

urlpatterns = [
    path('books/list', BookListView.as_view(), name='books-list'),
    path('books/create/<int:pk>/', BookCreateView.as_view(), name='books-create'),
    path('books/detail/<int:pk>/', BookDetailView.as_view(), name='books-detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='books-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='books-delete'),
]