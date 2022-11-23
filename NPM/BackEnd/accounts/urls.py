from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.addfields),
    path('mypage/', views.mypage),
    path('isLogin/', views.isLogin),
    path('get_user_data/', views.get_user_data),
]