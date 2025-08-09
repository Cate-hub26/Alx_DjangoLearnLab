from rest_framework import status, response.data
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')
        
        self.author = Author.objects.create(name='Clear')
        
        self.book = Book.objects.create(
            title='Atomic Habits', 
            publication_year=2018, 
            author=self.author)
        
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

    def test_delete_book(self):
        url = reverse('books_delete', args=[self.book.id])  # URL name for BookDeleteView
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

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

        
        
        
        
        
    
        
        
        
    

