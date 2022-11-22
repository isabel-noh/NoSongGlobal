from django.db import models
from django.conf import settings
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AbstractUser

# Create your models here.
# class Actor(models.Model):
#     # movie_id = models.ManyToManyField(Movie)
#     actor_name = models.TextField(blank=True, null=True, default=None)
#     profile_path = models.TextField(blank=True, null=True)
#     character = models.CharField(max_length=200)



class Genre(models.Model):
    genre_name = models.CharField(max_length=20)
    genre_id = models.IntegerField()

class Movie(models.Model):
    genre             = models.ManyToManyField(Genre, related_name='same_genre_movies')
    poster_path       = models.CharField(max_length=100, null=True)
    backdrop_path     = models.CharField(max_length=100, null=True)
    original_title    = models.CharField(max_length=100)
    title             = models.CharField(max_length=100)
    original_language = models.CharField(max_length=20)
    runtime           = models.IntegerField()
    revenue           = models.IntegerField()
    budget            = models.IntegerField()
    vote_count        = models.IntegerField()
    adult             = models.IntegerField()
    movie_id          = models.IntegerField()
    vote_average      = models.FloatField()
    popularity        = models.FloatField()
    release_date      = models.DateField()
    overview          = models.TextField(blank=True)