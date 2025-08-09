from rest_framework import status, response.data
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author

# BookAPITestCase is a class that contains testcases for CRUD Operations of the BookView
class BookAPITestCase(TestCase):
    """
Test suite for Book API endpoints.

This class covers CRUD operations for the Book model, including:
- Creating a book with valid data
- Updating an existing book
- Deleting a book
- Ensuring authentication is required for protected endpoints

Each test simulates API requests using Django's test client and verifies:
- Correct status codes
- Database changes
- Authentication enforcement
"""
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')
        
        # creates the author
        self.author = Author.objects.create(name='Clear')
        
        # creates the book
        self.book = Book.objects.create(
            title='Atomic Habits', 
            publication_year=2018, 
            author=self.author)
        
    # Test scenario for creating a book
    def test_create_book(self):
        url = reverse('books_create')
        
        data = {
            'title': 'The Mountain is You',
            'publication_year': 2016,
            'author': self.author.id
        }
        
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, 'The Mountain is You')
        
    # Test scenario for updating a book
    def test_update_book(self):
        url = reverse('books_update', args=[self.book.id])  # URL name for BookUpdateView
        data = {
            'title': 'Atomic Habits Revised',
            'publication_year': 2020,
            'author': self.author.id
        }
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Atomic Habits Revised')

    # Test scenario for deleting a book
    def test_delete_book(self):
        url = reverse('books_delete', args=[self.book.id])  # URL name for BookDeleteView
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
        
    # Testing authentication
    def test_authentication_required(self):
        self.client.logout()
        url = reverse('books_create')
        data = {
            'title': 'No Auth Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)  # Or 401 depending on your setup

        
        
        
        
        
    
        
        
        
    

