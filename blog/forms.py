from django import forms
from .models import Post, BookCategory, BookImage
from datetime import datetime

# EMPTY_CHOICE = (
#     ('', '-'*10),
# )

# CATEGORY_CHOICE = (
#     ('bungaku', '文学・評論'),
#     ('business', 'ビジネス・経済'),
#     ('nonfiction', 'ノンフィクション'),
#     ('science', 'サイエンス・テクノロジー')
# )

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


