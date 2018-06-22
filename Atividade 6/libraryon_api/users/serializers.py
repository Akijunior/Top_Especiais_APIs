from rest_framework import serializers

from .models import *


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('url', 'pk', 'name', 'age', 'books')


class LectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lector
        fields = ('url', 'pk', 'name', 'age')

