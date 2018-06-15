from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import *

usuario = User(name='Jun', email='ju@ju.com')
usuario.save()

from django.contrib.auth.models import User


import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

# Create your tests here.

class UserTestCase(APITestCase):

    def test_create_user(self):
        self.profile = User.objects.create_user("Ju", 'ju@ju.com', 'ju12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.profile)
        url = reverse('user-list')
        data = {'name': 'Kal El', 'email': 'kal@gmail.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(User.objects.get().email, 'ju@ju.com')


class CommentTestCase(APITestCase):

    def setUp(self):
        self.user = usuario
        self.profile = User.objects.create_user("Ju", 'ju@ju.com', 'ju12345')
        self.user.profiles.add(self.profile)
        self.client = APIClient()
        self.client.force_authenticate(user=self.profile)
        self.post = Post.objects.create(title="Post", body="New Post", owner=self.profile, userId=self.user)

    def test_user_can_create_a_comment(self):
        url = reverse('comment-list')
        data = {'name': 'New Comment', 'email': 'a@gmail.com',
                'body': 'Test hello world!', 'postId': self.post.id}
        response = self.client.post(url, data, format='json')
        # print("Response: ", response.json()) # status_text
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_update_a_comment(self):
        comment = Comment.objects.create(name='New Comment', email='a@gmail.com',
                body='Test hello world!', postId=self.post)
        url = reverse('comment-detail', kwargs={'pk': comment.id})
        data = {'name': 'New Comment'}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PostTestCase(APITestCase):

    def setUp(self):
        self.user = usuario
        self.profile = User.objects.create_user("Ju", 'ju@ju.com', 'ju12345')
        self.user.profiles.add(self.profile)
        self.client = APIClient()
        self.client.force_authenticate(user=self.profile)
        self.post = Post.objects.create(title="Post", body="New Post", owner=self.profile, userId=self.user)
        self.title = "Post"

    def test_user_can_create_a_post(self):
        url = reverse('post-list')
        post_data = {'owner': self.profile.id, 'userId': self.user.id,
                          'title': 'New Post', 'body': 'Test hello world!'}
        response = self.client.post(url, post_data, format='json')
        print("Response: ", response.json())
        print("Usuário: ", self.user.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_model_can_create_a_post(self):
        old_count = Post.objects.count()
        Post.objects.create(title="Post", body="New Post", owner=self.profile, userId=self.user)
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_returns_readable_representation(self):
        self.assertEqual(str(self.post), self.title)



class ViewTestCase(TestCase):

    def setUp(self):
        self.profile = User.objects.create_user("Ju", 'ju@ju.com', 'ju12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.profile)
        self.other_profile = User.objects.create_user("Ol", 'ol@ju.com', 'ol12345')
        self.user = usuario
        self.user.profiles.add(self.profile)

        self.post = Post(title="Post", owner=self.profile, userId=self.user)
        self.post.save()
        # self.client.login(username="Ju", password='ju12345')
        self.post_data = {"owner": self.profile.id, "userId": self.user.id,
                          "title": 'New Post', "body": 'Test hello world!'}
        self.response = self.client.post(
            reverse('post-list'),
            self.post_data,
            format="json"
        )

    def test_authorization_is_enforced(self):
        new_client = APIClient()
        response = new_client.get('/posts/', kwargs={'id': 3}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_post(self):
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
        change_post = {'title': 'New Post Title', 'owner': self.profile.id,
                       'userId': self.user.id, 'body': 'This field is required.'}
        response = self.client.put(
            reverse('post-detail', kwargs={'pk': post.id}),
            change_post, format="json"
        )
        print("Response: ", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_delete_a_own_post(self):
        post = Post.objects.get()
        response = self.client.delete(
            reverse('post-detail', kwargs={'pk': post.id}),
            format="json", follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
