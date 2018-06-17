from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import *


class PostListingField(serializers.RelatedField):
    def to_representation(self, value):
        return "Título: %s | Corpo: %s" % (value.title, value.body)

    def get_queryset(self):
        return Post.objects.all()
    # queryset = PostSerializer

class UserPostRelatedSerializer(serializers.ModelSerializer):
    user_posts = PostListingField(many=True)
    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

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

    def create(self, validated_data):
        posts_data = validated_data.pop('user_posts')
        post = Post.objects.create(**validated_data)
        for post_data in posts_data:
            Post.objects.create(post=post, **post_data)
        return post


class CommentSerializer(serializers.ModelSerializer):
    postId = serializers.ReadOnlyField(source='post.title')
    class Meta:
        model = Comment
        fields = ('url', 'name', 'email', 'body', 'postId')

    # url = serializers.HyperlinkedIdentityField(
    #     view_name="user:comment-detail",)

class PostSerializer(serializers.ModelSerializer):
    # userId = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name', read_only=True)
    # owner = serializers.ReadOnlyField()
    userId = serializers.ReadOnlyField(source='user.name')
    owner = serializers.ReadOnlyField(source='user.username')
    comments_count = serializers.SerializerMethodField()
    # comments_in_post = serializers.HyperlinkedRelatedField(many=True,
    #  view_name='user:comments-detail', read_only=True)

    def get_comments_count(self, obj):
        return obj.comments_in_post.count()

    class Meta:
        model = Post
        fields = ('owner', 'userId', 'url', 'title', 'body', 'comments_count')
    # comments_in_post = serializers.HyperlinkedRelatedField(
    # many=True, view_name='user:comment-detail', read_only=True)
    # comments_in_post = CommentSerializer(many=True, read_only=True)


# class UserPostsSerializer(serializers.ModelSerializer):
#     comments_in_post = serializers.HyperlinkedRelatedField(many=True, view_name='user:comment-detail', read_only=True)
#     userId = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
#     comments_count = serializers.SerializerMethodField()
#
#     def get_comments_count(self, obj):
#         return obj.comments_in_post.count()
#
#     class Meta:
#         model = Post
#         fields = ('url', 'title', 'body', 'userId', 'comments_in_post', 'comments_count')
#     # comments_in_post = CommentSerializer(many=True, read_only=True)







