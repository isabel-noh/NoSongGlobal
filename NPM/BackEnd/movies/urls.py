
from django.urls import path, include
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.movie_addall),
    path('movieList/', views.movie_list),
    path('movieList/<int:movie_pk>/', views.movie_detail),
    path('journal_all/', views.all),
    path('journal/create/', views.create),
    path('journal_all/<int:journal_pk>/', views.detail),
    # path('update/<int:journal_pk>/', views.update),
    # path('delete/<int:journal_pk>/', views.delete),
    path('journal/comment/create/<int:journal_pk>/', views.create_comment),
    path('journal/like/<int:journal_pk>/', views.like),
]