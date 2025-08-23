from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import CustomUser
from notifications.models import Notification

class NotificationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='user', password='pass123')
        self.actor = CustomUser.objects.create_user(username='actor', password='pass123')
        Notification.objects.create(
            recipient=self.user, actor=self.actor, verb='followed', target=None
        )

        self.client.force_authenticate(user=self.user)

    def test_fetch_notifications(self):
        url = reverse('notifications')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['notifications']), 1)
        self.assertEqual(response.data['notifications'][0]['verb'], 'followed')

