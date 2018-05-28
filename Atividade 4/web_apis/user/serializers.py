from rest_framework import serializers
from rest_framework.reverse import reverse

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


class UserPostsSerializer(serializers.ModelSerializer):
    comments_in_post = serializers.HyperlinkedRelatedField(many=True, view_name='user:comment-detail', read_only=True)
    # comments_in_post = CommentSerializer(many=True, read_only=True)
    userId = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    comments_count = serializers.SerializerMethodField()

    def get_comments_count(self, obj):
        return obj.comments_in_post.count()

    class Meta:
        model = Post
        fields = ('url', 'title', 'body', 'userId', 'comments_in_post', 'comments_count')



# class PostListingField(serializers.RelatedField):
#     queryset = PostSerializer.c
#     def to_representation(self, value):
#         return "Título: %s | Quantidade de comentários: %s" % (value.title, value.comments_count)


# class UserPostSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(
#         view_name="user:user-detail",
#     )
#
#     class Meta:
#         model = Post
#         fields = '__all__'


# class PostHyperlink(serializers.HyperlinkedRelatedField):
#     view_name = 'user:user-post-detail'
#     queryset = Post.objects.all()
#
#     def get_url(self, obj, view_name, request, format):
#         url_kwargs = {
#             'user_id': obj.userId,
#             'post_id': obj.pk,
#         }
#         return reverse(view_name, kwargs=url_kwargs, request=request, format=format)
#
#     def get_object(self, view_name, view_args, view_kwargs):
#         lookup_kwargs = {
#             'user__id': view_kwargs['user_id'],
#             'id': view_kwargs['post_id']
#         }
#         return self.get_queryset().get(**lookup_kwargs)


class UserSerializer(serializers.ModelSerializer):
    # user_posts = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='userId')
    # user_posts = serializers.StringRelatedField(many=True, read_only=True)
    # user_posts = PostSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="user:user-detail",
    )
    # user_posts = serializers.HyperlinkedRelatedField(many=True, view_name='user:post-detail', read_only=True)
    # user_posts = PostSerializer(many=True)
    # user_posts = PostHyperlink(many=True)

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

# class UserPostListSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(
#         view_name="user:user-detail",
#     )
#
#     class Meta:
#         model = Post
#         fields = ('url',)



