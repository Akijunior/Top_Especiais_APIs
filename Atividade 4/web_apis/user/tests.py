from django.core import serializers
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import *

usuario = User(name='Jun', email='ju@ju.com')
usuario.save()

from django.contrib.auth.models import User


# Create your tests here.

class ModelTestCase(TestCase):

    def setUp(self):
        self.post_title = ""
        self.post = Post(title=self.post_title)
        self.profile = User.objects.create_user("Nerd", 'ju@ju.com', 'ju12345')
        self.name = "Post"
        self.user = usuario

        self.post = Post(title=self.name, owner=self.profile, userId=self.user)

    def test_model_can_create_a_post(self):
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_returns_readable_representation(self):
        self.assertEqual(str(self.post), self.name)


class ViewTestCase(TestCase):

    def setUp(self):
        self.profile = User.objects.create_user("Ju", 'ju@ju.com', 'ju12345')
        self.user = usuario
        self.user.profiles.add(self.profile)

        self.post = Post(title="Post", owner=self.profile, userId=self.user)
        self.post.save()

        self.client = APIClient()
        self.client.force_authenticate(user=self.profile)

        self.post_data = {"title": 'New Post', "body": 'Test hello world!', "owner": self.profile.id,
                          "userId": self.user.id}
        self.response = self.client.post(
            reverse('post-list'),
            self.post_data,
            format="json"
        )

    def test_api_can_create_a_post(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        new_client = APIClient()
        response = new_client.get('/posts/', kwargs={'id': 3}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_post(self):
        print("O post é: ", self.post)
        response = self.client.get(
            '/posts/', kwargs={'pk': self.post.id}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.post)


    def test_user_not_can_update_a_post_from_other_user(self):
        post = Post.objects.get()
        change_post = {"title": "New Post Title"}
        response = self.client.put(
            reverse('post-detail', kwargs={'pk': post.id}),
            change_post, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_user_can_update_a_own_post(self):
        post = Post.objects.get()
        change_post = {"title": "New Post Title"}
        response = self.client.put(
            reverse('post-detail', kwargs={'pk': post.id}),
            change_post, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_delete_a_own_post(self):
        post = Post.objects.get()
        response = self.client.delete(
            reverse('post-detail', kwargs={'pk': post.id}),
            format="json", follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
