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
        serializer = UserAddFieldSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            print(serializer)
            return Response('우승')
        return Response('not valid')


@api_view(['GET'])
def mypage(request):
    # print(request.user) # username (email)
    # print(request.auth) # 사용자 토큰
    user = get_object_or_404(User, username=request.user)
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

#     # client로부터 온 데이터에서 비밀번호 갖고오기
#     password_1 = request.data.get('password1')
#     password_2 = request.data.get('password2')

#     # 회원가입 시 입력하는 비밀번호 다른 경우,
#     if password_1 != password_2:
#         return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

#     # 데이터 직렬화
#     serializer = UserSerializer(data=request.data)

#     # validation 진행
#     if serializer.is_valid(raise_exception=True):
#         user = serializer.save()
#         user.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def login(request):

#     serializer = UserSerializer(data=request.data)

#     if serializer.is_valid(raise_exception=True):
#         user = serializer
#         id = User.objects.get('username')
#         password = User.objects.get('password')
#         token = Token.objects.create(user=)

#         if id == request.data.get('username') and password == request.data.get('password'):




#             data = {
#             'nickname': nickname,
#             'token': token,  
#             }
#             return Response(data, status=)