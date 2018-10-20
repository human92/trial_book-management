from django import forms
from .models import Post, BookCategory

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
    class Meta:
        model = Post
        fields = ('title', 'text', 'category')
