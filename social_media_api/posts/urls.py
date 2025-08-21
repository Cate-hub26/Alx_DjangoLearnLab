from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet, CommentViewSet, FeedView,
    PostLikeView, PostUnlikeView
)
    

router = DefaultRouter()
router.register(r'Post', PostViewSet)
router.register(r'Comment', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('feed/', FeedView.as_view(), name='user-feed'),
    path('posts/<int:pk>/like/', PostLikeView.as_view(), name='post-like'),
    path('posts/<int:pk>/unlike/', PostUnlikeView.as_view(), name='post-unlike'),
]