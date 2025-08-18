from .views import RegisterUserView, CustomLoginView, UserProfileView
from django.urls import path

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]