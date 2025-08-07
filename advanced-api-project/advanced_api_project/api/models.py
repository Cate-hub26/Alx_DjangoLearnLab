from django.db import models

# The Author model represents a writer who can have many books
class Author(models.Model):
    
    # Each author has a name stored in a characters field.
    # The name of the author can have a maximum length of 200 characters.
    name = models.CharField(max_length=200)
    
# The Book model represents the books written by the Author.
# It consists of the book's title, publication_year, and its author.
class Book(models.Model):
    # The title of the book is limited to 200 characters.
    title = models.CharField(max_length=200)
    
    # The year the book was published as an Integer 
    publication_year = models.IntegerField()
    
    # ForeignKey create a one-to-many relationship: One author can have more than one book.
    # on_delete=models.CASCADE: Once the author is deleted, their books also deleted.
    # related_name='books' allows for reverse lookup: author.books.all() returns all the books by a given author.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
