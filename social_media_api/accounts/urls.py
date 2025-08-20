from .views import (
    RegisterUserView, CustomLoginView, 
    UserProfileView, FollowUserView, 
    UnfollowUserView
)
from django.urls import path

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
