from rest_framework import serializers

from users.models import Lector
from .models import *


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    lector = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Score
        fields = ('book', 'lector', 'score', 'comment', 'evaluation_date', 'last_update_date')

