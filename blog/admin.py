from django.contrib import admin
from .models import Post, BookCategory, BookImage

admin.site.register(Post)
admin.site.register(BookCategory)
admin.site.register(BookImage)

