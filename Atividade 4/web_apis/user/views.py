from rest_framework import renderers
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response

from user.permissions import IsOwnerOrReadOnly, IsOneProfileOfTheUserOrAccessDenied
from .serializers import *


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = (permissions.IsAuthenticated,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = (permissions.IsAuthenticated, IsOneProfileOfTheUserOrAccessDenied, )


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'
    permission_classes = (permissions.IsAuthenticated, )


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'
    permission_classes = (permissions.IsAuthenticated, )


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )


class UserRelatedViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPostRelatedSerializer


class UserPostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        try:
            user = User.objects.get(pk=self.kwargs.get('pk', None))

        except User.DoesNotExist:
            user = None

        posts = Post.objects.filter(userId=user.id)
        post = posts.filter(pk=self.kwargs.get('post_id', None))
        return post

    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, IsOwnerOrReadOnly,)


class UserPostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        try:
            user = User.objects.get(pk=self.kwargs.get('pk', None))

        except User.DoesNotExist:
            user = None

        posts = Post.objects.filter(userId=user.id)
        post = posts.get(pk=self.kwargs.get('post_id', None))
        comment = post.comments_in_post.filter(pk=self.kwargs.get('comment_id', None))
        return comment

    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, IsOwnerOrReadOnly,)


class UserPostComments(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        try:
            user = User.objects.get(pk=self.kwargs.get('pk', None))
        except User.DoesNotExist:
            user = None

        posts = Post.objects.filter(userId=user.id)
        post = posts.get(pk=self.kwargs.get('post_id', None))
        comments = post.comments_in_post
        return comments

    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, IsOwnerOrReadOnly,)


class PostHighlight(generics.GenericAPIView):
    queryset = Post.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(post.title)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserList.name, request=request),
            'posts': reverse(PostList.name, request=request),
            'comments': reverse(CommentList.name, request=request),
        })

# @api_view(['GET', 'POST'])
# def user_post_list(request, user_id):
#     if request.method == 'GET':
#         user = User.objects.get(id=user_id)
#         user_posts = user.user_posts.all()
#         user_posts_serializer = UserPostsSerializer(user_posts, many=True)
#         return Response(user_posts_serializer.data)
#
#     elif request.method == 'POST':
#         user_posts_serializer = UserPostsSerializer(data=request.data)
#         user_posts_serializer.save()
#         return Response(user_posts_serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_post_detail(request, user_id, post_id):
#     try:
#         user = User.objects.get(id=user_id)
#         user_posts = user.user_posts.all().get(id=post_id)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         user_post_serializer = UserPostsSerializer(user_posts, context={'request': request})
#         return Response(user_post_serializer.data)
#
#     elif request.method == 'PUT':
#         user_serializer = UserPostsSerializer(user, data=request.data)
#         user_serializer.save()
#         return Response(user_serializer.data, status=status.HTTP_201_CREATED)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     name = 'user-list'
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
#
#
# class UserDetail(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         try:
#             user = User.objects.get(pk=self.kwargs.get('user_id', None))
#
#         except User.DoesNotExist:
#             user = None
#
#         posts = Post.objects.filter(userId=user.id)
#         return posts


# def index(request):
#
#     dicio_json = {"""conteudo db.json"""}
#     dicio_string = json.dumps(dicio_json)
#     dicio_python = json.loads(dicio_string)
#     dicio_user = dicio_python["users"]
#
#     for i in dicio_user:
#         ...
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
#
#     # @action(methods=['post', 'get', 'put'], detail=True, url_path='posts', url_name='user_post_list')
#     #
#     # def user_post_list(self, request, pk=None):
#     #     user = self.get_object()
#     #     lista = user.user_posts.all()
#     #     # lista = PostSerializer.data.fget(user)
#     #     user_posts = []
#     #     for post in lista:
#     #         obj = model_to_dict(post)
#     #         user_posts.append(obj)
#     #     return Response(user_posts)
#
#     class Meta:
#         routes = {
#             "posts": 'PostViewSet',
#             "comments": 'CommentViewSet'
#         }
#
#
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     class Meta:
#         routes = {
#             "users": UserViewSet,
#         }
#
#
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


# class UserPostListViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = UserPostListSerializer
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_post_list(request, user_id):
#     try:
#         user = User.objects.get(id=user_id)
#         a = user.user_posts.all()
#         user_posts = []
#         for i in a:
#             user_posts.append(i)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         user_posts_serializer = UserPostListSerializer(user_posts, context={'request':request})
#         return Response(user_posts_serializer.data)


# class UserRequestViewSet(APIView):
#     def get(self, request, pk=None, format=None):
#         user = User.objects.get(pk=pk)
#         serializer_context = {
#             'request': request,
#         }
#         serializer = UserSerializer(user, context=serializer_context)
#         return Response(serializer.data)

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
