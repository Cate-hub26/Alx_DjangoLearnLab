#create.md
from bookshelf.models import Book
new_book = Book(title="1984", author="George Orwell", publication_year=1949)
new_book.save()

#Expected Output
1984

#retrieve.md
book = Book.objects.all()
print(book.author)

#Expected Output
George Orwell

#retrieve.md
book = Book.objects.all()
print(book.author)

#Expected Output
George Orwell

#delete.md
book.delete()

#Expected Output
(1, {'bookshelf.Book': 1})


