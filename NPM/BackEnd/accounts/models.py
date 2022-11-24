from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
class User(AbstractUser):
    # AbstractUser를 상속받는 커스텀 User 클래스 작성
    pass


class UserAddField(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=10, null=False)
    nickname = models.CharField(max_length=10, unique=True, null=False)
    profile_image = models.ImageField(max_length=100, upload_to="profile_%Y/%m/%d/", blank=True, null=True)