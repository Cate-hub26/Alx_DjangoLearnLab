from .models import Book, Library, Librarian, Author

#Query all books by a specific author
def books_by_specific_author(author_name):
    author = Author.objects.get(name=author_name)
    return Author.objects.filter(author=author)


#Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)


#List all books in a library
library = Library.books.all()

