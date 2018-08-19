from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework.request import Request

from .models import *
import datetime

class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ('url', 'title', 'description', 'isbn', 'edition', 'year',
                  'amount_pages', 'price', 'age_range', 'authors', 'genres', 'thumb',
                  'score_average')

    def validate_year(self, year):
        if year < 0.0:
            raise serializers.ValidationError("year cannot be an negative value")

        return year

    def validate_amount_pages(self, amount_pages):
        if amount_pages < 0:
            raise serializers.ValidationError("amount pages cannot be negative value")

        return amount_pages

    def validate_score(self, price):
        if price < 0.0:
            raise serializers.ValidationError("price cannot be an negative value")

        return price

class CreateGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name', 'description')


class GenreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Genre
        fields = ('url', 'name', 'description')

    def validate_name(self,name):
        return name
    def validate_description(self, description):
        return description

    def create(self, validated_data):
        genre = Genre.objects.create(name=validated_data['name'], description=validated_data['description'])
        genre.save()
        return genre

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    lector = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Score
        fields = ('url', 'book', 'lector', 'score', 'comment', 'evaluation_date', 'last_update_date')

    def validate_score(self, score):
        if score < 0.0:
            raise serializers.ValidationError("score cannot be an negative value")
        if score > 10.:
            raise serializers.ValidationError("10.0 is the max value of an score")
        return score

    def validate_comment(self, comment):
        if len(comment) < 5:
            raise serializers.ValidationError("the comment must have an minimum of 5 characters")

        return comment
