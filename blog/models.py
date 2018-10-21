from django.db import models
from django.utils import timezone

class BookCategory(models.Model):
    c_name = models.CharField(max_length=30)

    def __str__(self):
        return self.c_name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(BookCategory, on_delete=models.PROTECT)
    views_number = models.IntegerField(
            blank = True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    last_updated_date = models.DateTimeField(
            auto_now = True, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

