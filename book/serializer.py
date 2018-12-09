from rest_framework import serializers
from .models import Post, BookCategory
from django.contrib.auth.models import User

class UserSelializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class BookCategorySelializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ('__all__')

class PostSerializer(serializers.ModelSerializer):
    category = BookCategorySelializer()
    
    class Meta:
        model = Post
        fields = ('__all__')
