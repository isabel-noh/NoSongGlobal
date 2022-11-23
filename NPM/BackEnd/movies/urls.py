
from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    # path('', views.movie_addall),
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/like/', views.movie_like),
    path('data_collect/', views.data_collect),
    path('get_movie_data/', views.get_movie_data),
]