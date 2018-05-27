from httplib2 import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # @action(methods=['post', 'get', 'put'], detail=True, url_path='user_gram', url_name='user_gram')
    #
    # def user_gram(self, request, pk=None):
    #     user = self.get_object()
    #     return Response([post.title for post in user.user_posts.all()])

    class Meta:
        routes = {
            "posts": 'PostViewSet',
            "comments": 'CommentViewSet'
        }


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    class Meta:
        routes = {
            "users": UserViewSet,
        }


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def user_post_detail(request, user_id, post_id):
#     try:
#         user = User.objects.get(id=user_id)
#         user_posts = user.user_posts.all()
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         user_serializer = UserSerializer(user_posts)
#         return Response(user_serializer.data)
#
#     elif request.method == 'PUT':
#         game_serializer = UserSerializer(user, data=request.data)
#         game_serializer.save()
#         return Response(game_serializer.data, status=status.HTTP_201_CREATED)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class UserOperations(ListModelMixin, CreateModelMixin, RetrieveModelMixin,
#                              UpdateModelMixin, DestroyModelMixin, GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
# class CommentOperations(ListModelMixin, CreateModelMixin, RetrieveModelMixin,
#                              UpdateModelMixin, DestroyModelMixin, GenericAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
# class PostOperations(ListModelMixin, CreateModelMixin, RetrieveModelMixin,
#                              UpdateModelMixin, DestroyModelMixin, GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#     def post_detail(request, id):
#         try:
#             post = Post.objects.get(id=id)
#         except Post.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     name = 'user-detail'
#
# class ApiRoot(generics.GenericAPIView):
#     name = 'api-root'
#
#     def get(self, request, *args, **kwargs):
#         return Response({
#             'users': reverse('user-list', request=request),
#             'user-detail': reverse('user-detail', request=request),
#             'comments': reverse('comment-list', request=request),
#             'posts': reverse('post-list', request=request),
#         })


# @api_view(['GET', 'POST'])
# def game_list(request):
#     if request.method == 'GET':
#         games = User.objects.all()
#         games_serializer = GameSerializer(games, many=True)
#         return Response(games_serializer.data)
#     elif request.method == 'POST':
#         games_serializer = GameSerializer(data=request.data)
#         cont = Game.objects.all().count()
#         validador_de_entradas(games_serializer, cont)
#         return Response(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail(request, id):
#     try:
#         user = User.objects.get(id=id)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         user_serializer = UserSerializer(user)
#         return Response(user_serializer.data)
#
#     elif request.method == 'PUT':
#         user_serializer = UserSerializer(user, data=request.data)
#         user_serializer.save()
#         return Response(user_serializer.data, status=status.HTTP_201_CREATED)
