
from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_addall, name='movie_addall'),
    # path('actors/', views.actor_all, name='actor_all'),
    path('movieList/', views.movie_list),
    path('movieList/<int:movie_pk>/', views.movie_detail),
]