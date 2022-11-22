from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

from .models import Journal, Comment
from .serializers import JournalListSerializer, JournalSerializer, CommentSerializer



# Create your views here.


# 전체 저널 목록 제공
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def journals_all(request):
    # journals = Journal.objects.all()
    journals = get_list_or_404(Journal)
    serializer = JournalListSerializer(journals, many=True)
    return Response(serializer.data)
    

# 새로운 저널 생성
@api_view(['POST'])
@login_required
# @permission_classes([IsAuthenticated])
def journals_create(request):
    data = request.data
    photo = request.FILES
    # print(request.FILES)
    # print(photo['journal_image'])
    # 각 값을 journal model field에 맞게 저장


    journal = Journal(user=request.user, title= data['title'], content = data['content'], 
    movie_title = data['movie_title'], journal_image = photo['journal_image'], watched_at=data['watched_at'])
    journal.save()
    # print(journal)
    journal = Journal.objects.get(pk=journal.pk)
    serializer = JournalSerializer(journal, context={"request": request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
    

# 단일 저널 정보 제공 (정보 요청 정보에 따라 수정, 삭제 실행)
@api_view(['GET', 'PUT', 'DELETE'])
def journal_detail(request, journal_pk):
    # journal = Journal.objects.get(pk=journal_pk)
    journal = get_object_or_404(Journal, pk=journal_pk)

    if request.method == 'GET':
        serializer = JournalSerializer(journal)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = JournalSerializer(journal, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) 

    elif request.method == 'DELETE':
        journal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 댓글 생성
@api_view(['POST'])
def journal_comment_create(request, journal_pk):
    # journal = Journal.objects.get(pk=journal_id)
    journal = get_object_or_404(Journal, pk=journal_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(journal=journal)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



# 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def journal_like(request, journal_pk):
    if request.user.is_authenticated:
        journal = get_object_or_404(Journal, pk=journal_pk)
        user = request.user

        if journal.like_users.filter(pk=user.pk).exists():
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