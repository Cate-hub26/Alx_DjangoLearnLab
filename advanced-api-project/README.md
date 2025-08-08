
# Book API Views Overview

## BookListCreateView

**Class**: `ListCreateAPIView`  
**Model**: `Book`  
**Serializer**: `BookSerializer`  
**Permissions**: `IsAuthenticatedOrReadOnly`

### Purpose
Provides an endpoint to:
- List all books (`GET`)
- Create a new book (`POST`)

### Behavior
- **GET**: Accessible to all users. Returns a list of all book records.
- **POST**: Restricted to authenticated users. Allows creation of a new book.

## BookDetailUpdateDeleteView

**Class**: `RetrieveUpdateDestroyAPIView`  
**Model**: `Book`  
**Serializer**: `BookSerializer`  
**Permissions**: `IsAuthenticatedOrReadOnly`

### Purpose
Provides an endpoint to:
- Retrieve a single book (`GET`)
- Update a book (`PUT`/`PATCH`)
- Delete a book (`DELETE`)

### Behavior
- **GET**: Accessible to all users. Returns details of a specific book.
- **PUT/PATCH/DELETE**: Restricted to authenticated users. Allows modification or deletion of a book.
