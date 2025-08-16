from django.urls import path, include
from .views import (
    LoginView, LogoutView, ProfileView, SignUpView, profile_view,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, 
    PostDeleteView, CommentListView, CommentCreateView, CommentUpdateView,
    CommentDeleteView, posts_by_tag, search_posts
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
    path('post/<int:pk>delete/', PostDeleteView.as_view(), name='post-delete'),  
    path('post/<int:post_id>/comments/list/', CommentListView.as_view(), name='comment-list'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('post/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('tags/<tag_name>/', posts_by_tag, name='posts-by-tag'),
    path('search/<query>/', search_posts, name='posts-search'),
]
