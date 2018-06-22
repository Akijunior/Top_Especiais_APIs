from rest_framework import renderers
from rest_framework import viewsets, generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.throttling import ScopedRateThrottle

from users.permissions import *
from .serializers import *


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'
    permission_classes = (permissions.IsAuthenticated, ReadUserOnly, )


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'
    permission_classes = (permissions.IsAuthenticated, ReadUserOnly, )


class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    name = 'genre-list'
    permission_classes = (permissions.IsAuthenticated, ReadUserOnly, )


class GenreDetail(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    name = 'genre-detail'
    permission_classes = (permissions.IsAuthenticated, ReadUserOnly, )

