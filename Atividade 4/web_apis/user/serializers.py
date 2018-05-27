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
    comments_in_post = serializers.HyperlinkedRelatedField(many=True, view_name='user:comment-detail', read_only=True)
    # comments_in_post = CommentSerializer(many=True, read_only=True)
    userId = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    comments_count = serializers.SerializerMethodField()

    def get_comments_count(self, obj):
        return obj.comments_in_post.count()

    class Meta:
        model = Post
        fields = ('url', 'title', 'body', 'userId', 'comments_in_post', 'comments_count')


class UserSerializer(serializers.ModelSerializer):
    # user_posts = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='userId')
    # user_posts = serializers.StringRelatedField(many=True, read_only=True)
    # user_posts = PostSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="user:user-detail",
    )
    user_posts = serializers.HyperlinkedRelatedField(many=True, view_name='user:post-detail', read_only=True)

    posts_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_posts_count(self, obj):
        return obj.user_posts.count()

    def get_comments_count(self, obj):
        return Comment.objects.filter(postId__userId=obj).count()

    class Meta:
        model = User
        fields = ('pk', 'url', 'name', 'posts_count', 'comments_count', 'user_posts')
        # fields = ('pk', 'name', 'posts_count', 'comments_count')





