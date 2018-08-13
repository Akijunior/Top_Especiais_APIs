from django_filters.rest_framework import *
from rest_framework import filters, generics
from rest_framework.throttling import ScopedRateThrottle

from books.permissions import *
from .serializers import *


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


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'
    # permission_classes = [permissions.IsAuthenticated, ]
    throttle_scope = 'books-list'
    throttle_classes = [ScopedRateThrottle, ]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, ]

    filter_fields = ('title', 'year', 'price')
    search_fields = ('^title', 'year')
    ordering_fields = ('title', 'year')


class BookDetail(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'
    permission_classes = [permissions.IsAuthenticated, IsAuthorOfBookOrReadOnly, ]


class CreateBook(generics.CreateAPIView):
    name = 'create book'
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, OnlyAuthorCanCreateABook, ]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()


class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    name = 'genre-list'
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, ]

    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)


class GenreDetail(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    name = 'genre-detail'
    permission_classes = [permissions.IsAuthenticated]


class CreateGenre(generics.CreateAPIView):
    serializer_class = GenreSerializer
    name = 'create-genre'
    permission_classes = [IsAuthorOfBookOrReadOnly, permissions.IsAdminUser]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            ##return HttpResponse({"reason":"must be an Author to create genre"}, status=status.HTTP_401_UNAUTHORIZED)


class ScoreList(generics.ListAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-list'
    permission_classes = (permissions.IsAuthenticated,)
    throttle_scope = 'scores-list'
    throttle_classes = (ScopedRateThrottle,)

    def perform_create(self, serializer):
        serializer.save(lector=self.request.user)


class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-detail'
    permission_classes = [permissions.IsAuthenticated, OnlyTheLectorWhoAssignedTheScoreCanEditIt]


class CreateScore(generics.CreateAPIView):
    name = 'create-score'
    serializer_class = ScoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(lector=self.request.user)
