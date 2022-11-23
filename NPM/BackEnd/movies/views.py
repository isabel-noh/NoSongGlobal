import json

import requests
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
# permission Decorators
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# from .api import movies_json
from .models import Movie, Genre
from .serializers import MovieListSerializer, MovieSerializer, GenreListSerializer


# Authentication Decorators
# from rest_framework.decorators import authentication_classes

def data_collect(request):
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/now_playing'

    cur_page = 1
    movie_list = []

    # top-rated 
    while cur_page < 11:
        params = {
        'api_key': '7258d1fb8f49e6fdd21d6189e050655b',
        'language': 'ko',
        'page': cur_page,
        }
        res = requests.get(base_url + path, params=params)
        movie_list.extend(res.json()['results'])
        cur_page += 1
    

    cnt = 1
    for m in movie_list:
        id = m['id']
        path = f'/movie/{id}'
        params2 = {
        'api_key': '7258d1fb8f49e6fdd21d6189e050655b',
        'language': 'ko',
        }
        res = requests.get(base_url + path, params=params2).json()
        movie = {
            'poster_path' : m['poster_path'],
            'backdrop_path' : m['backdrop_path'],
            'original_title' : m['original_title'],
            'title' : m['title'],
            'original_language' : m['original_language'],
            'runtime' : res['runtime'],
            'revenue' : res['revenue'],
            'budget' : res['budget'],
            'vote_count' : m['vote_count'],
            'adult' : 1 if m['adult'] else 0,
            'movie_id' : m['id'],
            'vote_average' : m['vote_average'],
            'popularity' : m['popularity'],
            'release_date' : m['release_date'],
            'overview' : m['overview'],
        }
        movie = MovieListSerializer(data=movie)
        if movie.is_valid(raise_exception=True):
            movie2 = movie.save()
            for id in m['genre_ids']:
                genre = Genre.objects.get(genre_id=id)
                movie2.genre.add(genre)
            cnt += 1
    return Response(status=status.HTTP_201_CREATED)

def get_movie_data(request):
    # movies = get_list_or_404(Movie)
    # movie_titles = []
    # for movie in movies:
    #     movie_titles.append([movie.title, movie.pk])
    # return JsonResponse({'movie_titles': movie_titles})
    movies = get_list_or_404(Movie)
    movie_data = {}
    idx = 1
    for movie in movies:
        genre_id = [genre.genre_id for genre in get_object_or_404(Movie, id=movie.id).genre.all()]
        genre_text = [get_object_or_404(Genre, genre_id=id).genre_name for id in genre_id]
        movie_data[idx] = {
            'id' : movie.id,
            'title' : movie.title,
            'overview' : movie.overview,
            'poster_path' : movie.poster_path,
            'backdrop_path' : movie.backdrop_path,
            'runtime' : movie.runtime,
            'adult' : movie.adult,
            'vote_average' : movie.vote_average,
            'release_date' : movie.release_date,
            'genre_id' : genre_id,
            'genre_text' : genre_text,
            'revenue' : movie.revenue,
        }
        idx += 1
    return JsonResponse(movie_data, status=status.HTTP_200_OK)





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
    movie = get_object_or_404(Movie, pk=movie_pk)
    genre_id = [genre.genre_id for genre in get_object_or_404(Movie, id=movie.id).genre.all()]
    genre_text = [get_object_or_404(Genre, genre_id=id).genre_name for id in genre_id]
    movie_data = {
        'id' : movie.id,
        'title' : movie.title,
        'overview' : movie.overview,
        'poster_path' : movie.poster_path,
        'backdrop_path' : movie.backdrop_path,
        'runtime' : movie.runtime,
        'adult' : movie.adult,
        'vote_average' : movie.vote_average,
        'release_date' : movie.release_date,
        'genre_id' : genre_id,
        'genre_text' : genre_text,
        'revenue' : movie.revenue,
    }
    return Response(movie_data, status=status.HTTP_200_OK) 



