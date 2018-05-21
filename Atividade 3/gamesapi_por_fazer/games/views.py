"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework import generics, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Game, GameCategory, Player, Score
from .serializers import GameSerializer, GameCategorySerializer, PlayerSerializer, ScoreSerializer


# class ModelViewSet
# class GameCategoryList(generics.ListCreateAPIView):
class GameCategoryOperations(ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                             UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GameOperations(ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                             UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PlayerOperations(ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                             UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ScoreOperations(ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                             UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'players': reverse('player-list', request=request),
            'game-categories': reverse('game-category-list', request=request),
            'games': reverse('game-list', request=request),
            'scores': reverse('score-list', request=request)
        })

# @api_view(['GET', 'POST'])
# def game_list(request):
#     if request.method == 'GET':
#         games = Game.objects.all()
#         games_serializer = GameSerializer(games, many=True)
#         return Response(games_serializer.data)
#     elif request.method == 'POST':
#         games_serializer = GameSerializer(data=request.data)
#         if games_serializer.is_valid():
#             games_serializer.save()
#             return Response(games_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'POST', 'DELETE'])
# def game_detail(request, pk):
#     try:
#         game = Game.objects.get(pk=pk)
#     except Game.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         games_serializer = GameSerializer(game)
#         return Response(games_serializer.data)
#
#     elif request.method == 'PUT':
#         games_serializer = GameSerializer(game, data=request.data)
#         if games_serializer.is_valid():
#             games_serializer.save()
#             return Response(games_serializer.data)
#         return Response(games_serializer.erros, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         game.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
