from django.db import models
from django.conf import settings
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AbstractUser

# Create your models here.


class Genre(models.Model):
    # genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


# class Actor(models.Model):
#     # movie_id = models.ManyToManyField(Movie)
#     actor_name = models.TextField(blank=True, null=True, default=None)
#     profile_path = models.TextField(blank=True, null=True)
#     character = models.CharField(max_length=200)



class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    original_title = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    # actors = models.ManyToManyField(Actor)
    # actors = models.TextField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    poster_path = models.CharField(max_length=300, blank=True, null=True)
    backdrop_path = models.CharField(max_length=300, blank=True, null=True)
    genres = models.ManyToManyField(Genre)
    # genres = models.TextField(blank=True, null=True)



class Journal(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # movie_id = models.IntegerField()
    movie_title = models.CharField(max_length=100)
    # poster_path = models.CharField(max_length=300, blank=True, null=True)
    journal_image = models.FileField(upload_to=None, max_length=100, blank=True, null=True)
    watched_at = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_journals')


class Comment(models.Model):
    content = models.TextField()
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)