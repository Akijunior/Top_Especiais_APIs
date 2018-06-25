from rest_framework import generics

from books.permissions import *
from .serializers import *


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'
    permission_classes = (permissions.IsAuthenticated, OnlyAuthorCanCreateABook,)

    def perform_create(self, serializer):
        author = Author.objects.get(auth_profile=self.request.user)
        authors = []
        authors.append(author)
        serializer.save(authors=authors)


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'
    permission_classes = (permissions.IsAuthenticated, IsAuthorOfBookOrReadOnly,)


class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    name = 'genre-list'
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)


class GenreDetail(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    name = 'genre-detail'
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)


class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-list'
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(lector=self.request.user)


class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-detail'
    permission_classes = (permissions.IsAuthenticated, OnlyTheLectorWhoAssignedTheScoreCanEditIt,)
