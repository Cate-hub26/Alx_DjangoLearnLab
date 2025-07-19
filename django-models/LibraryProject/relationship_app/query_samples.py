#Query all books by a specific author
from .models import Book, Library, Librarian
Book.objects.filter(author='authorname')

#List all books in a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)  # <- required line
    return Librarian.objects.get(library=library)

Library.objects.get(library='library_name')
books = Book.objects.all()
books.all()

#Retrieve the librarian for a library
Librarian.objects.get(name='librarian_name', library='library_name')

