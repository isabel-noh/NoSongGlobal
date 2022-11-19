from rest_framework import serializers
from .models import Movie, Genre

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    # 단일 영화 정보 제공 
    class Meta:
        model = Movie
        fields = '__all__'


# class ActorListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actor
#         field = '__all__'