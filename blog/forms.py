from django import forms
from .models import Post, BookCategory, BookImage
from datetime import datetime

class PostForm(forms.ModelForm):
    title = forms.TextInput
    text = forms.Textarea
    category = forms.ModelChoiceField(queryset=BookCategory.objects.all())
    image_name = forms.CharField()
    image = forms.ImageField()
    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'image_name', 'image')

class ImgForm(forms.ModelForm):
    # image = forms.ImageField()
    class Meta:
        model = BookImage
        fields = ('img_name', 'img')


