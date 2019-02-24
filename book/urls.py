from rest_framework import routers
from django.conf.urls import include, url
from .views import BookCategoryViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'book_category', BookCategoryViewSet)
router.register(r'posts', PostViewSet)

