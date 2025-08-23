# 📱 Social Media API

A lightweight, modular Django REST API for building social media features — including user authentication, profile management, posts, comments, follows, likes, notifications, and a personalized feed.

---

## 🚀 Features Implemented (Tasks 0–5)

### **0. Project Setup & User Authentication**
- Django project (`social_media_api`) with Django REST Framework
- Custom `User` model extending `AbstractUser`:
  - `bio` (TextField)
  - `profile_picture` (ImageField → `media/profile_pics/`)
  - `followers` & `following` (ManyToMany to self, `symmetrical=False`)
- Token-based authentication (`rest_framework.authtoken`)
- Endpoints:
  - **Register** (returns token)
  - **Login** (returns token)
  - **Profile retrieval**

### **1. Posts & Comments**
- **Post model**: `author`, `title`, `content`, timestamps
- **Comment model**: linked to `Post` and `User`, with timestamps
- CRUD operations for posts and comments
- Permissions: only authors can edit/delete their own content
- Pagination for large datasets
- Filtering posts by `title` or `content`

### **2. User Follows & Feed**
- **Follow system**:
  - Users can follow/unfollow others
  - `following` relationship stored in custom user model
- **Feed endpoint**:
  - Aggregates posts from followed users
  - Ordered by creation date (newest first)
- Permissions: users can only modify their own following list

### **3. Likes & Notifications**
- **Like system**:
  - Users can like/unlike posts
  - Prevents duplicate likes
- **Notification system**:
  - Generic model using `ContentType` for flexible targets
  - Triggers on:
    - New follower
    - Post liked
    - Post commented
  - Stores `recipient`, `actor`, `verb`, `target`, `timestamp`, `is_read`
- Endpoints:
  - Liking/unliking posts
  - Viewing notifications (unread first)

---

## 🛠 Tech Stack

- **Backend:** Django + Django REST Framework
- **Auth:** Token-based authentication
- **Database:** SQLite (default, configurable)
- **Media:** Profile pictures stored in `media/profile_pics/`

---

## 📂 Project Structure

social_media_api/
├── accounts/         # User registration, login, profile, follows
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests/        # Unit tests for accounts app
├── posts/            # Post, comment, like models, views, feed
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests/        # Unit tests for posts app
├── notifications/    # Notification model, views, serializers
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests/        # Unit tests for notifications app
├──  db        
├── 
└── manage.py


---

## 🔐 Authentication Workflow Example

This API uses **token-based authentication** via `rest_framework.authtoken`. Below is a step-by-step guide to registering, logging in, and accessing protected endpoints.

### 📝 1. Register a New User

```http
POST /api/register/
Content-Type: application/json

{
  "username": "nzisa_dev",
  "password": "securePass123",
  "email": "nzisa@example.com",
  "bio": "Backend engineer & API enthusiast"
}```


### Response

{
  "token": "abc123xyz456tokenvalue"
}


 ---

### 🔐 2. Login

```http
POST /api/login/
Content-Type: application/json

{
  "username": "nzisa_dev",
  "password": "securePass123"
}

### Response

{
  "token": "abc123xyz456tokenvalue"
}


--

### 🔒 3. Access Protected Endpoints

GET /api/profile/
Authorization: Token abc123xyz456tokenvalue

### Response

{
  "username": "nzisa_dev",
  "email": "nzisa@example.com",
  "bio": "Backend engineer & API enthusiast",
  "followers": [],
  "following": [],
  "profile_picture": null
}