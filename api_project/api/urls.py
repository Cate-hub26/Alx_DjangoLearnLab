from django.urls import path, include
from .views import BookListCreateAPIView, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('', include(router.urls)),
]