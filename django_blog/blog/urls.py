from django.urls import path, include
from .views import LoginView, LogoutView, ProfileView, SignUpView, profile_view

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/', profile_view, name='profile'),

]

