from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter
from django_filters.rest_framework import *
from rest_framework import filters, generics
from rest_framework.throttling import ScopedRateThrottle

from books.permissions import *
from .serializers import *


from rest_framework.renderers import DocumentationRenderer


class CustomRenderer(DocumentationRenderer):
    languages = ['ruby', 'go']

class ScoreFilter(filters.BaseFilterBackend):
    min_score = NumberFilter(
        name='score', lookup_expr='gte')
    max_score = NumberFilter(
        name='score', lookup_expr='lte')
    from_score_date = DateTimeFilter(
        name='evaluation_date', lookup_expr='gte')
    to_score_date = DateTimeFilter(
        name='evaluation_date', lookup_expr='lte')
    player_name = AllValuesFilter(
        name='lector__name')
    game_name = AllValuesFilter(
        name='book__title')

    class Meta:
        model = Score
    fields = ('score', 'from_score_date', 'to_score_date',
              'min_score', 'max_score', 'lector_name', 'book_title')


class BookList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing books.

    post:
    Create a new book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'
    permission_classes = (permissions.IsAuthenticated, OnlyAuthorCanCreateABook, ViewBookPermissions,)
    throttle_scope = 'books-list'
    throttle_classes = (ScopedRateThrottle,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, filters.DjangoObjectPermissionsFilter,)

    filter_fields = ('title', 'year', 'price')
    search_fields = ('^title', 'year')
    ordering_fields = ('title', 'year')

    # def perform_create(self, serializer):
    #     author = Author.objects.get(auth_profile=self.request.user)
    #     authors = Author.objects.filter(name="Hello")
    #     authors.all().add
    #     serializer.save(authors=authors)


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'
    permission_classes = (permissions.IsAuthenticated, IsAuthorOfBookOrReadOnly,)


class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    name = 'genre-list'
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, )

    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)


class GenreDetail(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    name = 'genre-detail'
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)


class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-list'
    permission_classes = (permissions.IsAuthenticated, )
    throttle_scope = 'scores-list'
    throttle_classes = (ScopedRateThrottle, )

    def perform_create(self, serializer):
        serializer.save(lector=self.request.user)


class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-detail'
    permission_classes = (permissions.IsAuthenticated, OnlyTheLectorWhoAssignedTheScoreCanEditIt, )
