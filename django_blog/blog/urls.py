from django.urls import path, include
from .views import (
    LoginView, LogoutView, ProfileView, SignUpView, profile_view,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, 
    PostDeleteView
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
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 

]
