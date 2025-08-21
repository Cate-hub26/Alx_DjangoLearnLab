from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, permissions
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from rest_framework.views import APIView


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['post']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        # Get users the current user is following
        
        following_users = request.user.following.all()
        
        # Get posts from those users, ordered by newest first
        
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        
        # Serialize and return the data
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class PostLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def like_post(request,post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user
    
        if Like.objects.filter(user=user, post=post).exists():
           return Response({'detail': 'You have already liked this post.'}, status=400)
    
        Like.objects.create(user=user, post=post)
    
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb='liked your post',
                target=post,
                target_content_type=ContentType.objects.get_for_model(post),
               target_object_id=post.id
            )
        return Response({'detail': 'Post liked successfully.'}, status=201)

class PostUnlikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def unlike_post(request,post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user
    
        like = Like.objects.create(user=user, post=post).first()
    
        if not like:
            return Response({'detail': 'You have not liked this post.'}, status=400)
    
        like.delete()
        return Response({'detail': 'Post unliked successfully.'}, status=200)

    
