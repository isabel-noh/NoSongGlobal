from rest_framework import serializers
from .models import Journal, Comment


# 전체 저널 목록 제공
class JournalListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = ('title',)


# 해당 저널의 댓글 목록 제공
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content',)


# 단일 저널 정보 제공
class JournalSerializer(serializers.ModelSerializer):

    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Journal
        fields = ('title', 'content',)