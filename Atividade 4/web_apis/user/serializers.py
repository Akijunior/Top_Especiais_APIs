from rest_framework import serializers

from .models import *


class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="user:comment-detail",
    )
    class Meta:
        model = Comment
        fields = ('url', 'name', 'email', 'body', 'postId')


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="user:post-detail",
    )
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('url', 'title', 'body', 'userId', 'comments')


class UserSerializer(serializers.ModelSerializer):
    # user_posts = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='userId')
    # user_posts = serializers.StringRelatedField(many=True, read_only=True)
    # user_posts = PostSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="user:user-detail",
    )
    user_posts = serializers.HyperlinkedRelatedField(many=True, view_name='user:post-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url', 'name', 'email', 'addressId', 'user_posts')





