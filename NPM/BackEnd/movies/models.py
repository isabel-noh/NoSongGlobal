from django.db import models

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


