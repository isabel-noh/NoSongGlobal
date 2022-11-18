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
from .serializers import MovieListSerializer


# Authentication Decorators
# from rest_framework.decorators import authentication_classes

url = "https://api.themoviedb.org/3/movie/popular?api_key=9aef886051103d6c65ad737f677114e5&language=ko-KR&page="
@api_view(['POST'])
def movie_addall(request):
    for page in range(1, 6): # 원하는 페이지 만큼 돌림
        res = requests.get(url+str(page))
        text = res.text
        movies_json = json.loads(text)['results']
        Movies = movies_json
        for movie_1 in Movies:
            a = Movie(
                movie_id=movie_1['id'],
                title=movie_1['title'],
                original_title=movie_1['original_title'],
                overview=movie_1['overview'],
                poster_path=movie_1['poster_path'],
                backdrop_path=movie_1['backdrop_path'],
                release_date=movie_1['release_date'],
                vote_average=movie_1['vote_average'],
                popularity=movie_1['popularity'],
                genres=json.dumps(movie_1['genre_ids'])
            )
            a.save()
    return Response(request)