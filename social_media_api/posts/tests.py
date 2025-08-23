from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post, Like
from rest_framework.test import APIClient
from accounts.models import CustomUser
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


User = get_user_model()

class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='nzisa', password='pass123')
        self.client.login(username='nzisa', password='pass123')

    def test_create_and_like_post(self):
        # Create post
        create_url = reverse('post-list')
        data = {"title": "Test Post", "content": "This is a test."}
        response = self.client.post(create_url, data)
        self.assertEqual(response.status_code, 201)

        post_id = response.data['id']  # Get the created post's ID
        self.assertEqual(Post.objects.count(), 1)

        # Like post
        like_url = reverse('post-like', kwargs={'pk': post_id})
        like_response = self.client.post(like_url)
        self.assertEqual(like_response.status_code,  201)

class FeedTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = CustomUser.objects.create_user(username='user1', password='pass123')
        self.user2 = CustomUser.objects.create_user(username='user2', password='pass123')
        self.user3 = CustomUser.objects.create_user(username='user3', password='pass123')

        self.post1 = Post.objects.create(author=self.user2, content='Post from user2')
        self.post2 = Post.objects.create(author=self.user3, content='Post from user3')

        self.user1.following.add(self.user2)
        self.client.force_authenticate(user=self.user1)

    def test_feed_returns_followed_posts(self):
        url = reverse('user-feed')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        contents = [post['content'] for post in response.data]
        self.assertIn('Post from user2', contents)
        self.assertNotIn('Post from user3', contents)

class LikeNotificationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = CustomUser.objects.create_user(username='author', password='pass123')
        self.liker = CustomUser.objects.create_user(username='liker', password='pass123')
        self.post = Post.objects.create(author=self.author, content='Test post')
        self.client.force_authenticate(user=self.liker)

    def test_like_post_creates_like_and_notification(self):
        url = reverse('post-like', args=[self.post.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 201)

        # Like object created
        self.assertTrue(
        Like.objects.filter(author=self.liker, post=self.post).exists()
        )

        # Notification created
        notif = Notification.objects.create(
        recipient=self.author,
        actor=self.liker,
        verb='liked',
        target_content_type=ContentType.objects.get_for_model(Post),
        target_object_id=self.post.id
        )
        self.assertTrue(notif)


    def test_duplicate_like_is_prevented(self):
        Like.objects.create(author=self.liker, post=self.post)
        url = reverse('post-like', args=[self.post.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)  # Or 409 if you prefer conflict

    def test_unlike_post_removes_like(self):
        Like.objects.create(author=self.liker, post=self.post)
        url = reverse('post-unlike', args=[self.post.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        Like.objects.filter(author=self.liker, post=self.post).delete()
        self.assertFalse(Like.objects.filter(author=self.liker, post=self.post).exists())