from django.shortcuts import get_object_or_404
from .serializers import RegisterUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from .models import CustomUser

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)
        
        if target_user == request.user:
            return Response(
                {'error': "You can't follow yourself."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        request.user.following.add(target_user)
        return Response(
            {'message': f'You are now following {target_user.username}.'}, 
            status=status.HTTP_200_OK
        )
        
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)
        
        if target_user == request.user:
            return Response(
                {'error': "You can't unfollow yourself."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        request.user.following.remove(target_user)
        return Response(
            {'message': f'You have unfollowed {target_user.username}.'}, 
            status=status.HTTP_200_OK
        )
         
class RegisterUserView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username
        })
        
class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        serializer = RegisterUserSerializer(request.user)
        return Response(serializer.data)
        


        
        
