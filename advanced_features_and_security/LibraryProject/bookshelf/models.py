from django.db import models
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, BaseUserManager, AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    groups = models.ManyToManyField(
        Group,
        related_name='bookshelf_user_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='bookshelf_user_permissions'
    )
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        pass
    def create_superuser(self, email, password=None):
        pass
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
       
class Book(models.Model):    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField(null=True, blank=True)
    
    class Meta:
        permissions = (
            ('can_view', 'Can view'),
            ('can_create', 'Can create'),
            ('can_edit', 'Can edit'),
            ('can_delete', 'Can delete'),
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
    user = models.OneToOneField(CustomUser, related_name='userprofile', on_delete=models.CASCADE)
    role = models.CharField(max_length=200, choices=Role_Choices)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"
