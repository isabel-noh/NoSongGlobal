from rest_framework import serializers
from .models import Journal, Comment


# 전체 저널 목록 제공
class JournalListSerializer(serializers.ModelSerializer):

    # username = serializers.CharField(source='user.username', read_only=True)
    journal_image = serializers.ImageField(use_url=True)
    class Meta:
        model = Journal
        fields = ('title', 'pk', 'movie_id', 'watched_at', 'journal_image', 'user_id')

# 해당 저널의 댓글 목록 제공
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


# 단일 저널 정보 제공
class JournalSerializer(serializers.ModelSerializer):

    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Journal
        fields = '__all__'
        read_only_fields = ('nickname', 'comment_set', 'comment_count', 'like_users')
