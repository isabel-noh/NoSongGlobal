from django.db import models
from django.conf import settings
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator

# from movies.models import Movie

# Create your models here.

class Journal(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie       = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    journal_image = models.ImageField(upload_to="%Y/%m/%d/", max_length=100, blank=True, null=True)
    watched_at = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_journals')
    rank        = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])


class Comment(models.Model):
    content = models.TextField()
    journal_pk = models.ForeignKey(Journal, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)