from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.reverse import reverse

from books.views import *
from .serializers import *


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-list'
    # # permission_classes = [permissions.IsAuthenticated, ReadUserOnly, TokenHasReadWriteScope]
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, ]

    filter_fields = ('name', 'age')
    search_fields = ('^name',)
    ordering_fields = ('name', 'age')


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-detail'
    # # permission_classes = [permissions.IsAuthenticated, ReadUserOnly, TokenHasReadWriteScope,]
    # permission_classes = [permissions.IsAuthenticated, ]


class AuthorCreate(generics.CreateAPIView):
    queryset = Lector.objects.all()
    name = "new-author"
    serializer_class = CreateAuthorSerializer
    # permission_classes = [permissions.IsAdminUser, ]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()


class LectorList(generics.ListAPIView):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    name = 'lector-list'
    #    permission_classe s = (permissions.IsAuthenticated, ReadUserOnly, TokenHasReadWriteScope, )
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, ]


class LectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    name = 'lector-detail'
    #    # permission_classes = (permissions.IsAuthenticated, ReadUserOnly, TokenHasReadWriteScope, )
    # permission_classes = [permissions.IsAuthenticated]


class LectorCreate(generics.CreateAPIView):
    queryset = Lector.objects.all()
    name = "new-lector"
    serializer_class = CreateLectorSerializer
    throttle_scope = 'create-profile-throttle'
    throttle_classes = [ScopedRateThrottle, ]
    # permission_classes = []
    authentication_classes = []

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()


class CustomAuthToken(ObtainAuthToken):
    throttle_scope = 'api-token'
    throttle_classes = [ScopedRateThrottle]
    name = 'obtain_custom_auth_token'

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user_id': user.id,
            'user_name': user.username,
            'token': token.key,
        })


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserList.name, request=request),
            'authors': reverse(AuthorList.name, request=request),
            'lectors': reverse(LectorList.name, request=request),
            'books': reverse(BookList.name, request=request),
            'genres': reverse(GenreList.name, request=request),
            'scores': reverse(ScoreList.name, request=request),
            'new-scores': reverse(NewScoreList.name, request=request),
        })
