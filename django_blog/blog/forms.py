from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from taggit.forms import TagField
from taggit.forms import TagWidget


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']  
        
class PostForm(forms.ModelForm):
    tags = TagField(required=False, widgets=TagWidget())
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']