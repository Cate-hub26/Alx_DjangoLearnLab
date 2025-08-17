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
    tags = TagField(required=False, widget=TagWidget())
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Write your content here...'}),
        }

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']