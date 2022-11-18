from rest_framework import serializers
from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        field = '__all__'