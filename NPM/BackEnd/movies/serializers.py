from rest_framework import serializers
from .models import Movie, Genre, Journal, Comment


# 전체 영화 목록 
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


# 전체 장르 목록
class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


# 단일 영화 정보 제공 
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


# 출연 배우 목록 제공
# class ActorListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actor
#         field = '__all__'





# 전체 저널 목록 제공
class JournalListSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Journal
        fields = ('title', 'poster_path')




# 해당 저널의 댓글 목록 제공
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content',)


# 단일 저널 정보 제공
class JournalSerializer(serializers.ModelSerializer):

    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Journal
        fields = ('title', 'content', 'comment_set', 'comment_count', 'username',)
        read_only_fields = ('user', )