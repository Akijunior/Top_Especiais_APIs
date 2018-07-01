from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse

from users.permissions import *
from .serializers import *

from books.views import *
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter
from django_filters.rest_framework import *

from rest_framework import filters, generics, renderers, status, viewsets, generics, permissions
from rest_framework.throttling import ScopedRateThrottle

from django.contrib import admin
admin.autodiscover()

from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-list'
    #permission_classes = [permissions.IsAuthenticated, ReadUserOnly, TokenHasReadWriteScope]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,]

    filter_fields = ('name', 'age')
    search_fields = ('^name',)
    ordering_fields = ('name', 'age')


class AuthorDetail(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-detail'
    #permission_classes = [permissions.IsAuthenticated, ReadUserOnly, TokenHasReadWriteScope,]
    permission_classes = [permissions.IsAuthenticated,]

class AuthorCreate(generics.CreateAPIView):
    queryset = Lector.objects.all()
    name = "new-author"
    serializer_class = CreateAuthorSerializer
    permission_classes = [permissions.IsAdminUser, ]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()


class LectorList(generics.ListAPIView):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    name = 'lector-list'
#    permission_classes = (permissions.IsAuthenticated, ReadUserOnly, TokenHasReadWriteScope, )
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,]



class LectorDetail(generics.RetrieveAPIView):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    name = 'lector-detail'
#    permission_classes = (permissions.IsAuthenticated, ReadUserOnly, TokenHasReadWriteScope, )
    permission_classes = [permissions.IsAuthenticated]


class LectorCreate(generics.CreateAPIView):
    queryset = Lector.objects.all()
    name = "new-lector"
    serializer_class = LectorSerializer
    permission_classes = []
    authentication_classes = []

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()

class CustomAuthToken(ObtainAuthToken):

    throttle_scope = 'api-token'
    throttle_classes = [ScopedRateThrottle]
    name = 'obtain custom auth token'

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
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
            'users': reverse(AuthorList.name, request=request),
            'lectors': reverse(LectorList.name, request=request),
            'books': reverse(BookList.name, request=request),
            'genres': reverse(GenreList.name, request=request),
            'scores': reverse(ScoreList.name, request=request),
        })
