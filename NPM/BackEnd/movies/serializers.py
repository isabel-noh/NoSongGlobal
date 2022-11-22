from rest_framework import serializers
from .models import Movie, Genre


# 전체 영화 목록 
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('genre',)


# 전체 장르 목록
class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
        


# 단일 영화 정보 제공 
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


# 출연 배우 목록 제공
# class ActorListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actor
#         field = '__all__'

