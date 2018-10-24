from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, BookCategory, BookImage
from .forms import PostForm, ImgForm
from django.shortcuts import redirect
from datetime import datetime

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views_number += 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        # img_form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.image = form.cleaned_data['image']
            post.save()
            return redirect(post_detail, pk=post.pk)
        # if img_form.is_valid():
        #     img_form.img = form.cleaned_data['img']
        #     img_form.save()
        #     return redirect(post_detail, pk=post.pk)
    else:
        form = PostForm()
        # img_form = ImgForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    # return render(request, 'blog/post_edit.html', {'form': form, 'img_form':img_form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        # img_form = ImgForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.image = form.cleaned_data['image']
            post.save()
            return redirect(post_detail, pk=post.pk)
        # if img_form.is_valid():
        #     img_form.img = form.cleaned_data['img']
        #     img_form.save()
        #     return redirect(post_detail, pk=post.pk)
    else:
        form = PostForm(instance=post)
        # img_form = ImgForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    # return render(request, 'blog/post_edit.html', {'form': form, 'img_form':img_form})

