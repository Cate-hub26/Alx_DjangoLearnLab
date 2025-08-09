from django.urls import path
from .views import (BookListView, BookCreateView, 
BookDetailView, BookUpdateView, BookDeleteView)

urlpatterns = [
    path('books/list', BookListView.as_view(), name='books_list'),
    path('books/create', BookCreateView.as_view(), name='books_create'),
    path('books/detail/<int:pk>/', BookDetailView.as_view(), name='books_detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='books_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='books_delete'),
]