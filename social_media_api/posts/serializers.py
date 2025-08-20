from .models import Post, Comment
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta():
        model = Post
        fields = ['author', 'title', 'content', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        # Author will be set from request context
            
        user = self.context['request'].user
        return Post.objects.create(user=user, **validated_data)
            
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    
    class Meta():
        model = Comment
        fields = ['author', 'post', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        user = self.context['request'].user
        return Comment.objects.create(user=user, **validated_data)
        
            