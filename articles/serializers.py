from rest_framework import serializers
from .models import (
    Article, 
    Comment, 
)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('article')
        return ret

class ArticleSerializer(serializers.ModelSerializer) :
    author = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True, required=False)

    class Meta :
        model=Article
        fields='__all__'
        read_only_fields = ('author',)

class ArticleDetailSerializer(ArticleSerializer):
    comments= CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)