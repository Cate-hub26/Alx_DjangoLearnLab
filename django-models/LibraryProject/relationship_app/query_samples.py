#Query all books by a specific author
from .models import Book, Library, Librarian
Book.objects.filter(author='authorname')

#List all books in a library
Library.objects.all()

#Retrieve the librarian for a library
Librarian.objects.get(name='librarianname', library='libraryname')

