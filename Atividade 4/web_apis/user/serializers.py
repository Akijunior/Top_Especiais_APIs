from rest_framework import serializers

from .models import *


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'name', 'email', 'body', 'postId')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('url', 'title', 'body', 'userId', 'comments')


class UserSerializer(serializers.ModelSerializer):
    user_posts = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='userId')
    class Meta:
        model = User
        fields = ('url', 'name', 'email', 'addressId', 'user_posts')





