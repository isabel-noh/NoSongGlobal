import json

import requests
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
# permission Decorators
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from .api import movies_json
from .models import Movie
from .serializers import MovieListSerializer, MovieSerializer


# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# url = "https://api.themoviedb.org/3/movie/popular?api_key=9aef886051103d6c65ad737f677114e5&language=ko-KR&page="
# # @api_view(['POST'])
# def movie_addall(request):
#     for page in range(1, 6): # 원하는 페이지 만큼 돌림
#         res = requests.get(url+str(page))
#         text = res.text
#         movies_json = json.loads(text)['results']
#         Movies = movies_json

#         for movie_1 in Movies:
#             movie_id = movie_1['id']
#             credit_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=9aef886051103d6c65ad737f677114e5'
#             credit_data = requests.get(credit_url).json()
#             cast_data = credit_data['cast']

#             for cast in cast_data:
#                 i = Actor(
#                     # movie_id = movie_1['id'],
#                     actor_name = cast['name'],
#                     profile_path = cast['profile_path'],
#                     character = cast['character'],
#                 )
#                 i.save()
            
#             a = Movie(
#                 movie_id = movie_1['id'],
#                 title = movie_1['title'],
#                 original_title = movie_1['original_title'],
#                 overview = movie_1['overview'],
#                 poster_path = movie_1['poster_path'],
#                 backdrop_path = movie_1['backdrop_path'],
#                 release_date = movie_1['release_date'],
#                 vote_average = movie_1['vote_average'],
#                 popularity = movie_1['popularity'],
#                 genres = json.dumps(movie_1['genre_ids']),
#                 actors = Actor.actor_name
#             )
#             a.save()
        
#     return Response(request)



url = "https://api.themoviedb.org/3/movie/popular?api_key=9aef886051103d6c65ad737f677114e5&language=ko-KR&page="
@api_view(['GET', 'POST'])
def movie_addall(request):
    for page in range(1, 6): # 원하는 페이지 만큼 돌림
        res = requests.get(url+str(page))
        text = res.text
        movies_json = json.loads(text)['results']
        Movies = movies_json

        for movie_1 in Movies:
            # movie_id = movie_1['id']
            # credit_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=9aef886051103d6c65ad737f677114e5'
            # credit_data = requests.get(credit_url).json()
            # cast_data = credit_data['cast']
            # actors1 = {}
            # n = 1
            # for cast in cast_data:
                # i = Actor(
                #     # movie_id = movie_1['id'],
                #     actor_name = cast['name'],
                #     profile_path = cast['profile_path'],
                #     character = cast['character'],
                # )
                # i.save()
                # actors1[n] = cast['name']
                # n += 1
                
            a = Movie(
                movie_id = movie_1['id'],
                title = movie_1['title'],
                original_title = movie_1['original_title'],
                overview = movie_1['overview'],
                poster_path = movie_1['poster_path'],
                backdrop_path = movie_1['backdrop_path'],
                release_date = movie_1['release_date'],
                vote_average = movie_1['vote_average'],
                popularity = movie_1['popularity'],
                genres = json.dumps(movie_1['genre_ids']),
                # actors = json.dumps(actors1),
            )
            a.save()
    # print(actors1)
    return Response(request)



@api_view(['GET'])
def movie_list(request):
    # 전체 영화 목록 제공
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    # 단일 영화 정보 제공 
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data) 