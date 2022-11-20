
from django.urls import path, include
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.movie_addall),
    path('movieList/', views.movie_list),
    path('movieList/<int:movie_pk>/', views.movie_detail),
]