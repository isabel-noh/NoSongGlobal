from django.urls import path, include
from . import views

app_name = 'journal'

urlpatterns = [
    path('all/', views.all),
    path('create/', views.create),
    path('<int:journal_pk>/', views.detail),
    # path('update/<int:journal_pk>/', views.update),
    # path('delete/<int:journal_pk>/', views.delete),
    path('comment/create/<int:journal_pk>/', views.create_comment),
    path('like/<int:journal_pk>/', views.like),
]