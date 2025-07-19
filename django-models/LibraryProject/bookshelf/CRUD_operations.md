```python

#create.md
from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

#retrieve.md
Book.objects.get(title="1984")

#update.md
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.title = "Nineteen Eighty-Four"
book.save()

#delete.md
from bookshelf.models import Book
book.delete()





