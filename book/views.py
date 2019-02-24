from datetime import datetime
from django.utils import timezone
from .models import Post, BookCategory
import django_filters
from rest_framework import viewsets, filters
from .serializer import PostSerializer, BookCategorySelializer


class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySelializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

