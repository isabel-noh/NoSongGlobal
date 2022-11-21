from django.db import models
from django.conf import settings


# Create your models here.

class Journal(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # movie_id = models.IntegerField()
    movie_title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=300, blank=True, null=True)
    watched_at = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_journals')


class Comment(models.Model):
    content = models.TextField()
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)