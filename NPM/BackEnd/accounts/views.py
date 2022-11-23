from django.shortcuts import render, get_object_or_404
# from django.contrib.auth import login as auth_login
# from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_POST, require_http_methods
# from django.http import JsonResponse
# from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User, UserAddField
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
def mypage(request):
    print('1',request.data) 
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