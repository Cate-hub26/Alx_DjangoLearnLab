from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import CustomUser

User = get_user_model()

class AuthenticationTests(APITestCase):
    def test_user_registration(self):
        data = {
            "username": "nzisa",
            "password": "securepass123",
            "email": "nzisa@example.com"
        }
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("token", response.data)

    def test_login_with_valid_credentials(self):
        User.objects.create_user(username="nzisa", password="securepass123")
        data = {"username": "nzisa", "password": "securepass123"}
        response = self.client.post("/api/login/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

class FollowTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = CustomUser.objects.create_user(username='user1', password='pass123')
        self.user2 = CustomUser.objects.create_user(username='user2', password='pass123')
        self.client.force_authenticate(user=self.user1)

    def test_follow_user(self):
        url = reverse('follow-user', args=[self.user2.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user2, self.user1.following.all())

    def test_unfollow_user(self):
        self.user1.following.add(self.user2)
        url = reverse('unfollow-user', args=[self.user2.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(self.user2, self.user1.following.all())