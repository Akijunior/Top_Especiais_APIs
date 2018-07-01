import re

from django.contrib.auth.models import User
from rest_framework import serializers

from .permissions import *
from .models import *

# SETTINGS

VALIDATE_VALID_EMAIL_REGEX = True
EMAIL_VALIDATE_REGEX = r"[^@]+@[^@]+\.[^@]+"
MIN_PASSWORD_LENGHT = 4

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:

        model = Author
        
        books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='books-detail'
    )

        fields = ('url', 'pk', 'name', 'age', 'books', 'email', 'password')

    def validate_age(self, age):
        if age < 0:
            raise serializers.ValidationError("age cannot be negative or null value")
        return age

    def validate_email(self, email):
        if not re.match(EMAIL_VALIDATE_REGEX, email) and VALIDATE_VALID_EMAIL_REGEX:
            raise serializers.ValidationError("this is not an valid email address")

        if User.objects.filter(username=email).exists():
            raise serializers.ValidationError("this email has already token")

        return email

    def validate_books(self, books):
        if books is None:
            return None

    def validate_password(self, password):
        if len(password) < MIN_PASSWORD_LENGHT:
            raise serializers.ValidationError("password must have %s characters at least" % MIN_PASSWORD_LENGHT)
        return password

    def create(self, validated_data):
        auth_profile = User.objects.create_user(username=validated_data['email'], email=validated_data['email'],
                                                  password=validated_data['password'])
        auth_profile.save()
        author = Author.objects.create(name=validated_data['name'], email=validated_data['email'],
                                       age=validated_data['age'], auth_profile=auth_profile)
        author.save()
        return author


class CreateAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('url', 'pk', 'name', 'age', 'email', 'password')

    def validate_age(self, age):
        if age < 0:
            raise serializers.ValidationError("age cannot be negative or null value")
        return age

    def validate_email(self, email):
        if not re.match(EMAIL_VALIDATE_REGEX, email) and VALIDATE_VALID_EMAIL_REGEX:
            raise serializers.ValidationError("this is not an valid email address")

        if User.objects.filter(username=email).exists():
            raise serializers.ValidationError("this email has already token")

        return email

    def validate_books(self, books):
        if books is None:
            return None

    def validate_password(self, password):
        if len(password) < MIN_PASSWORD_LENGHT:
            raise serializers.ValidationError("password must have %s characters at least" % MIN_PASSWORD_LENGHT)
        return password

    def create(self, validated_data):
        auth_profile = User.objects.create_user(username=validated_data['email'], email=validated_data['email'],
                                                  password=validated_data['password'])
        auth_profile.save()
        author = Author.objects.create(name=validated_data['name'], email=validated_data['email'],
                                       age=validated_data['age'], auth_profile=auth_profile)
        author.save()
        return author


class LectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lector
        fields = ('url', 'pk', 'name', 'age', 'email', 'password')

    def validate_age(self, age):
        if age < 0:
            raise serializers.ValidationError("age cannot be negative or null value")
        return age

    def validate_email(self, email):
        if not re.match(EMAIL_VALIDATE_REGEX, email) and VALIDATE_VALID_EMAIL_REGEX:
            raise serializers.ValidationError("this is not an valid email address")

        if User.objects.filter(username=email).exists():
            raise serializers.ValidationError("this email has already token")

        return email

    def validate_password(self, password):
        if len(password) < MIN_PASSWORD_LENGHT:
            raise serializers.ValidationError("password must have %s characters at least" % MIN_PASSWORD_LENGHT)
        return password

    def create(self, validated_data):
        lector_profile = User.objects.create_user(username=validated_data['email'], email=validated_data['email'],
                                                  password=validated_data['password'])
        lector_profile.save()
        lector = Lector.objects.create(name=validated_data['name'], email=validated_data['email'],
                                       age=validated_data['age'], lector_profile=lector_profile)
        lector.save()

        return lector
