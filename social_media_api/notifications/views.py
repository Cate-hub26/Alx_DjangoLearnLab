from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        all_notifications = Notification.objects.filter(recipient=user)
        unread_notifications = all_notifications.filter(is_read=False)
        
        data = {
            'unread_count': unread_notifications.count(),
            'notifications': [
                {
                    'id': n.id,
                    'actor': n.actor.username,
                    'verb': n.verb,
                    'target_type': n.target_content_type.model,
                    'target_id': n.target_object_id,
                    'timestamp': n.timestamp
                } for n in all_notifications
            ]
        }
        return Response(data)

        
        
        
