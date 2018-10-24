from django.db import models
from django.utils import timezone

class BookCategory(models.Model):
    c_name = models.CharField(max_length=30)

    def __str__(self):
        return self.c_name


class BookImage(models.Model):
        img_name = models.CharField(max_length=50)
        img = models.ImageField(upload_to='blog')

        def __str__(self):
                return self.img_name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(BookCategory, on_delete=models.PROTECT)
    views_number = models.PositiveIntegerField(
            default=0, blank=True, null=True)
    text = models.TextField()
    img_name = models.CharField(max_length=50, null=True)
    img = models.ImageField(upload_to='blog', null=True)
    #imag_id = models.ForeignKey(BookImage, on_delete=models.PROTECT, null=True)
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    last_updated_date = models.DateTimeField(
            auto_now=True, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

