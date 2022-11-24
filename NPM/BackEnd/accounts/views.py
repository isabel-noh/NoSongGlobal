from django.shortcuts import render, get_object_or_404, get_list_or_404
# from django.contrib.auth import login as auth_login
# from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_POST, require_http_methods
# from django.http import JsonResponse
# from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from .models import User, UserAddField
from journals.models import Journal
from movies.models import Movie
from .serializers import UserAddFieldSerializer, UserSerializer

# # Create your views here.
@api_view(['POST'])
@csrf_exempt
def addfields(request):
    if request.method == 'POST':
        user = get_object_or_404(get_user_model(), username=request.user)
        data = request.data
        user_add = UserAddField(user=request.user, name=data['name'], nickname=data['nickname'], 
        like_ost_genre=data['like_ost_genre'], profile_image=request.FILES.get('profile_image'))
        user_add.save()
        user_add = UserAddField.objects.get(name=data['name'])
        serializer = UserAddFieldSerializer(data=user_add)
        return Response('not valid')



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def mypage(request):
    print('1', request.data) 
    # # username (email)
    print('2',request.auth) 
    # # 사용자 토큰
    user = get_object_or_404(User, username=request.user)
    # user = get_object_or_404(User)
    print(user)
    add = get_object_or_404(UserAddField, user=user.id)
    serializer_user = UserSerializer(user)
    serializer_add = UserAddFieldSerializer(add)
    # print(serializer_user.data) -> 로그인한 사람의 기본 정보
    # print(serializer_add.data) -> 로그인한 사람의 추가 정보
    context = {
        'serializer_user': serializer_user.data,
        'serializer_add': serializer_add.data,
    }
    return Response(context)


@api_view(['GET'])
def isLogin(request):
    user = get_object_or_404(User, username=request.user)
    add = get_object_or_404(UserAddField, user=user.id)
    # 닉네임, 로그인 상태, 유저 번호 보내기
    # user -> is_active, id
    # add -> nickname
    serializer_user = UserSerializer(user)
    serializer_add = UserAddFieldSerializer(add)
    context = {
        'user_id': serializer_user.data['id'],
        'is_active': serializer_user.data['is_active'],
        'nickname': serializer_add.data['nickname'],
    }
    return Response(context)

@api_view(['POST'])
def get_user_data(request):
    users = get_list_or_404(User)
    len_users = len(users)
    movies = get_list_or_404(Movie)
    len_movies = len(movies)
    all_users_data = {}
    print('id', request.user.id)
    for user in users:
        rating_list = []
        for idx in range(1, len_movies+1):
            journals = list(filter(lambda x: (x.user_id==user.id and x.movie_id==idx), get_list_or_404(Journal)))
            rating = sum([journal.rank for journal in journals]) / len(journals) if journals else 2.5
            rating_list.append([rating, idx])
        all_users_data[user.id] = rating_list

    similarity = []
    for other_user in range(1, len_users+1):
        if other_user == request.user.id:
            continue
        tot = 0
        for movie_idx in range(len_movies):
            tot += abs(all_users_data[other_user][movie_idx][0] - all_users_data[request.user.id][movie_idx][0]) ** 3
        similarity.append([tot, other_user])
    similarity.sort()
    
    recommend_movie_list = []


    # 유저 수가 적어서 유사도가 높은 유저순으로 4점 넘게 준 영화들의 목록을 recommend_movie_list에 담아 5개까지만 담아
    # 위 영화들을 추천해주는 형식
    # 이를 업그레이드 한다면 유사도가 높은 상위 N% 유저들이 매긴 영화 평점들의 평균을 구해 평균 평점이 높은 영화 5개를 추천
    for idx, sim in enumerate(similarity):
        print(idx)
        if len(recommend_movie_list) >= 5:
            break
        simillar_user = sim[1]
        for movie in sorted(all_users_data[simillar_user], reverse=True):
            print(movie)
            movie_rate, movie_id = movie
            if movie_rate < 4:
                break
            recommend_movie_list.append(movie_id)
            if len(recommend_movie_list) >= 5:
                break
    print(recommend_movie_list)

    return Response({'recommendMovieList' : recommend_movie_list}, status=status.HTTP_200_OK)






#             data = {
#             'nickname': nickname,
#             'token': token,  
#             }
#             return Response(data, status=)