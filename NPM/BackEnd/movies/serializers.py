from rest_framework import serializers
from .models import Movie, Genre

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        field = '__all__'


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        field = '__all__'