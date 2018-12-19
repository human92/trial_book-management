from rest_framework import serializers
from .models import Post, BookCategory
from django.contrib.auth.models import User
import json

class UserSelializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class BookCategorySelializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ('id', 'c_name')
        extra_kwargs = { 'id': { 'read_only': False } }

class PostSerializer(serializers.ModelSerializer):
    category = BookCategorySelializer()
    
    class Meta:
        model = Post
        fields = ('author', 'title', 'category', 'views_number', 'text', 'img_name', 'img', 
        'created_date', 'published_date', 'last_updated_date')
    
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        posted = BookCategory.objects.get(pk=category_data['id'])
        post = Post.objects.create(category=posted, **validated_data)
        return post
