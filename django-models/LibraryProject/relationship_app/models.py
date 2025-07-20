from django.db import models
from django.contrib.auth import User
from django.contrib.auth.decorators import user_passes_test, permission_required

class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
@permission_required        
class Book(models.Model):    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    class Meta():
        permissions = ('can_add_book', 'can_change_book', 'can_delete_book')
    
    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')
    
    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
@user_passes_test
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile')
    role = models.CharField(max_length=200, choices=('Admin', 'Librarian', 'Member'))
