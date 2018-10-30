from django import forms
from .models import Post, BookCategory
from datetime import datetime

class PostForm(forms.ModelForm):
    title = forms.TextInput
    text = forms.Textarea
    category = forms.ModelChoiceField(queryset=BookCategory.objects.all())
    img_name = forms.CharField()
    img = forms.ImageField()
    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'img_name', 'img')


