
# Book API Views Overview

## BookListView

**Class**: `ListAPIView`  
**Model**: `Book`  
**Serializer**: `BookSerializer`  
**Permissions**: `IsAuthenticatedOrReadOnly`

### Purpose
Provides an endpoint to:
- List all books (`GET`)

### Behavior
- **GET**: Accessible to all users. Returns a list of all book records.

## BookCreateView

**Class**: `CreateAPIView`  
**Model**: `Book`  
**Serializer**: `BookSerializer`  
**Permissions**: `IsAuthenticatedOrReadOnly`

### Purpose
Provides an endpoint to:
- Create a new book (`POST`)

### Behavior
- **POST**: Restricted to authenticated users. Allows creation of a new book.

## BookDetailView

**Class**: `RetrieveAPIView`  
**Model**: `Book`  
**Serializer**: `BookSerializer`  
**Permissions**: `IsAuthenticatedOrReadOnly`

### Purpose
Provides an endpoint to:
- Retrieve a single book (`GET`)

### Behavior
- **GET**: Accessible to all users. Returns details of a specific book.

## BookUpdateView

**Class**: `UpdateAPIView`  
**Model**: `Book`  
**Serializer**: `BookSerializer`  
**Permissions**: `IsAuthenticatedOrReadOnly`

### Purpose
Provides an endpoint to:
- Update a book (`PUT`/`PATCH`)

### Behavior
- **PUT/PATCH**: Restricted to authenticated users. Allows modification or deletion of a book.

## BookDeleteView

**Class**: `DestroyAPIView`  
**Model**: `Book`  
**Serializer**: `BookSerializer`  
**Permissions**: `IsAuthenticatedOrReadOnly`

### Purpose
Provides an endpoint to:
- Delete a book (`DELETE`)

### Behavior
- **DELETE**: Restricted to authenticated users. Allows modification or deletion of a book.