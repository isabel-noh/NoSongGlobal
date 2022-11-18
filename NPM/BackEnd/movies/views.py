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
        print(page)
        for movie_1 in Movies: # 모델컬럼에 맞춰서 저장해야함
            a = Movie(title = movie_1['title'], release_date = movie_1['release_date'], popularity = movie_1['popularity'], overview = movie_1['overview'], poster_path=movie_1['poster_path'])
            a.save()
    return Response(request)
# movie_addall()