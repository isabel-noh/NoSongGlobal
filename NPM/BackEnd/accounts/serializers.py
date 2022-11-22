from rest_framework import serializers
# from django.contrib.auth import get_user_model
from .models import User, UserAddField


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserAddFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddField
        fields = ()