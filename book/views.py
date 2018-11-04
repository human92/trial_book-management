# from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.utils import timezone
from .models import Post, BookCategory
import django_filters
from rest_framework import viewsets, filters
from .serializer import PostSerializer, BookCategorySelializer
# from .forms import PostForm
# from django.shortcuts import redirect

class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySelializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'book/post_list.html', {'posts': posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.views_number += 1
#     post.save()
#     return render(request, 'book/post_detail.html', {'post': post})

# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.img = form.cleaned_data['img']
#             post.save()
#             return redirect(post_detail, pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'book/post_edit.html', {'form': form})

# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.img = form.cleaned_data['img']
#             post.save()
#             return redirect(post_detail, pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'book/post_edit.html', {'form': form})
