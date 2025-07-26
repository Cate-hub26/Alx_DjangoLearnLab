from django.db import models
from django.contrib import admin
from django.contrib.auth import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import permission_required

from django.db import models
from django.contrib.auth import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.decorators import permission_required

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, date_of_birth, profile_photo):
        pass
    def create_superuser(self, email, password=None, date_of_birth, profile_photo):
        pass
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
@permission_required        
class Book(models.Model):    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    class Meta:
        permissions = (
            ('can_add_book', 'Can add a book'),
            ('can_change_book', 'Can change a book'),
            ('can_delete_book', 'Can delete a book'),
        )
    
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
    
class UserProfile(models.Model):
    Role_Choices = (
    ('Admin', 'Administrator'),
    ('Librarian', 'Library Staff'),
    ('Member', 'Registered Member'),
    )
    user = models.OneToOneField(CustomUser, related_name='userprofile')
    role = models.CharField(max_length=200, choices=Role_Choices)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
