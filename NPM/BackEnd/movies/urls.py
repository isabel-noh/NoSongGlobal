
from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_addall, name='movie_addall'),

]