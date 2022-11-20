from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Journal, Comment
from .serializers import JournalListSerializer, JournalSerializer, CommentSerializer



# Create your views here.


# 전체 저널 목록 제공 & 저널 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def all(request):
    request.method == 'GET':
    # journals = Journal.objects.all()
    journals = get_list_or_404(Journal)
    serializer = JournalListSerializer(journals, many=True)
    return Response(serializer.data)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    request.method == 'POST':
    serializer = JournalSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        data = {
            'Create' : '게시글이 작성되었습니다.'
        }
        return Response(data, serializer.data, status=status.HTTP_201_CREATED)
    
    

# 단일 저널 정보 제공 (정보 요청 정보에 따라 수정, 삭제 실행)
@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, journal_id):
    # journal = Journal.objects.get(pk=journal_pk)
    journal = get_object_or_404(Journal, pk=journal_id)

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
        data = {
            'Delete' : f'{journal_id}번째 게시글이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# 댓글 생성
@api_view(['POST'])
def create_comment(request, journal_id):
    # journal = Journal.objects.get(pk=journal_id)
    journal = get_object_or_404(Journal, pk=journal_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(journal=journal)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



# 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like(request, journal_id):
    if request.user.is_authenticated:
        journal = get_object_or_404(Journal, pk=journal_id)
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