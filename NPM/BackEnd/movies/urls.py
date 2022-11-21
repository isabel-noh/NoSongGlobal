
from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    # path('', views.movie_addall),
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
]