from rest_framework import serializers
# from django.contrib.auth import get_user_model
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'profile_image', 'nickname', 'email', 'name')