from django.urls import path, include
from . import views

app_name = 'journals'

urlpatterns = [
    path('', views.journals_all),
    path('create/', views.journals_create),
    path('<int:journal_pk>/detail/', views.journal_detail),
    path('<int:journal_pk>/like/', views.journal_like),
    path('<int:journal_pk>/comment/create/', views.journal_comment_create),
    path('<int:journal_pk>/comment/all/', views.journal_comment_all),
]