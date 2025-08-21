from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser

class Post(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='posts'
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} by {self.author.username}"
    
class Comment(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
    
class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes'
    )
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='likes'
    )

    def __str__(self):
        return f"{self.author.username} liked Post {self.post.id}"
        