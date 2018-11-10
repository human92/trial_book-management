from rest_framework import serializers
from .models import Post, BookCategory

class BookCategorySelializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ('c_name')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'img_name', 'img', 'created_date')
