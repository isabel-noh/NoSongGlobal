
from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_addall, name='movie_addall'),
#     path('<int:movie_pk>/', views.detail, name='detail'),
#     path('recommended/', views.recommended, name='recommended'),
]