from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    addressId = models.ForeignKey('Address', related_name='users_in_address',on_delete=models.CASCADE)
    profiles = models.ManyToManyField('auth.User')

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.street


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    body = models.CharField(max_length=300)
    postId = models.ForeignKey('Post', related_name='comments_in_post', verbose_name='Todos os comentários',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    userId = models.ForeignKey('User', related_name='user_posts',on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
