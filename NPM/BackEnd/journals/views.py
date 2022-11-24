from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

from .models import Journal, Comment
from .serializers import JournalListSerializer, JournalSerializer, CommentSerializer
from movies.models import Movie


# Create your views here.


# 전체 저널 목록 제공
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def journals_all(request):
    # journals = Journal.objects.all()
    journals = get_list_or_404(Journal)
    serializer = JournalListSerializer(journals, many=True)
    journal_data_all = []
    for i in serializer.data:
        # movie_poster = get_list_or_404(Movie, movie_id=i['movie_id']).poster_path
        # movie_poster = Movie.objects.get(movie_id=i['movie_id'])
        movie_poster = Movie.objects.get(id=i['movie_id']).poster_path
        journal_data = {
            'id': i['pk'],
            'title': i['title'],
            'movie_id': i['movie_id'],
            'watched_at': i['watched_at'],
            'journal_image': i['journal_image'],
            'poster_path': movie_poster,
        }
        journal_data_all.append(journal_data)
    return Response(journal_data_all, status=status.HTTP_200_OK)
    

# 새로운 저널 생성
@api_view(['POST'])
@login_required
# @permission_classes([IsAuthenticated])
def journals_create(request):
    data = request.data
    # request.FILES.get -> 이미지 안 넣어도 넘어갈 수 있음.
    # 각 값을 journal model field에 맞게 저장
    print(request.data)
    journal = Journal(user=request.user, title= data['title'], content = data['content'], 
    movie_id=int(data['movie_id']), movie_title=data['movie_title'], journal_image=request.FILES.get('journal_image'),
    watched_at=data['watched_at'], rank=int(data['journal_rank']))
    journal.save()
    journal = Journal.objects.get(pk=journal.pk)
    serializer = JournalSerializer(journal, context={"request": request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
    

# 단일 저널 정보 제공 (정보 요청 정보에 따라 수정, 삭제 실행)
@api_view(['GET', 'PUT', 'DELETE'])
def journal_detail(request, journal_pk):
    journal = get_object_or_404(Journal, pk=journal_pk)
    
    if request.method == 'GET':
        serializer = JournalSerializer(journal)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = JournalSerializer(journal, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 

    elif request.method == 'DELETE':
        journal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 댓글 생성
@api_view(['POST'])
def journal_comment_create(request, journal_pk):
    # journal = get_object_or_404(Journal, pk=journal_pk)

    comment = Comment(
        content = request.data['comment'],
        journal_pk_id = journal_pk,
        user_id = request.user.id
    )
    comment.save()
    serializer = CommentSerializer(comment)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


# 해당 게시글의 댓글들 가져오기
@api_view(['GET'])
def journal_comment_all(request, journal_pk):
    return Response()


# 좋아요
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def journal_like(request, journal_pk):
    if request.user.is_authenticated:
        journal = get_object_or_404(Journal, pk=journal_pk)
        user = request.user

        if journal.like_users.filter(id=user.id).exists():
            journal.like_users.remove(user)
            is_liked = False
        else:
            journal.like_users.add(user)
            is_liked = True

        like_count = journal.like_users.count()

        context = {
            'is_Liked': is_liked,
            'like_count': like_count,
        }
        return Response(context)
