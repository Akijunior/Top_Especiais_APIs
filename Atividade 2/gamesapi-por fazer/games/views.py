"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from games.models import Game
from games.serializers import GameSerializer
from django.utils import timezone


@api_view(['GET', 'POST'])
def game_list(request):
    if request.method == 'GET':
        games = Game.objects.all()
        games_serializer = GameSerializer(games, many=True)
        return Response(games_serializer.data)
    elif request.method == 'POST':
        games_serializer = GameSerializer(data=request.data)
        cont = Game.objects.all().count()
        validador_de_entradas(games_serializer, cont)
        return Response(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def game_detail(request, id):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        return Response(game_serializer.data)

    elif request.method == 'PUT':
        game_serializer = GameSerializer(game, data=request.data)
        validador_de_entradas(game_serializer, id)
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if game.release_date > timezone.now():
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('O jogo em questão já foi lançado, por isso não pode ser excluído!',
                        status=status.HTTP_400_BAD_REQUEST)


def validador_de_entradas(game_serializer, id_pk):
    game = Game.objects.get(id=id_pk)
    if game_serializer.is_valid():
        if game.name == None:
            return Response('O nome do jogo não pode ficar nulo', status=status.HTTP_400_BAD_REQUEST)
        elif game.game_category == None:
            return Response('A categoria do jogo não pode ser nula', status=status.HTTP_400_BAD_REQUEST)
        elif game.release_date == None:
            return Response('A data de lançamento não pode ser nula', status=status.HTTP_400_BAD_REQUEST)
        else:
            game_serializer.save()
            return Response(game_serializer.data, status=status.HTTP_201_CREATED)
