from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
class User(AbstractUser):
    # AbstractUser를 상속받는 커스텀 User 클래스 작성
    name = models.CharField(max_length=10, null=True)
    nickname = models.CharField(max_length=10, unique=True, null=True)
    profile_image = models.ImageField(null=True)
    like_ost_genre = models.CharField(max_length=10, default='', blank=True)