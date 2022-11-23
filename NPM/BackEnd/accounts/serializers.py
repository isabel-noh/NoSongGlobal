from rest_framework import serializers
# from django.contrib.auth import get_user_model
from .models import User, UserAddField


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserAddFieldSerializer(serializers.ModelSerializer):

    profile_image = serializers.ImageField(use_url=True)
    user = serializers.CharField(source='user.username')
    class Meta:
        model = UserAddField
        fields = '__all__'
        read_only_fields = ('user', 'profile_image',)
