from django.urls import path, include
from .views import (
    LoginView, LogoutView, ProfileView, SignUpView, profile_view,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, 
    PostDeleteView, CommentListView, CommentCreateView, CommentUpdateView,
    CommentDeleteView
)

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/', profile_view, name='profile'),
    path('post/', PostListView.as_view(), name='post-list'),                 
    path('post/new/', PostCreateView.as_view(), name='post-create'),         
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),    
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),   
    path('posts/<int:post_id>/comments/list/', CommentListView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:pk>/comments/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('posts/<int:pk>/comments/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
