from django.utils import timezone
from rest_framework import serializers

from .models import Game, GameCategory, Score, Player


class GameSerializer(serializers.ModelSerializer):
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')
    class Meta:
        model = Game
        fields = ('url', 'name', 'game_category', 'release_date', 'played')


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameCategory
        fields = ('url', 'pk', 'name', 'games')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field='name', allow_null=True)
    player = serializers.SlugRelatedField(queryset=Player.objects.all(), slug_field='name', allow_null=True)

    def validate(self, dados):
        if dados['player'] == None:
            raise serializers.ValidationError("É necessário que haja um player selecionado para validação do score.")
        if dados['game'] == None:
            raise serializers.ValidationError("É necessário que haja um game selecionado para validação do score.")
        if dados['score'] < 0 or dados['score'] == None:
            raise serializers.ValidationError("O score não pode ser nulo nem negativo.")
        if dados['score_date'] > timezone.now():
            raise serializers.ValidationError("A data do score não pode estar no futuro.")
        return dados

    class Meta:
        model = Score
        fields = ('url', 'pk', 'score', 'score_date', 'player', 'game',)


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('url', 'name', 'gender', 'scores',)