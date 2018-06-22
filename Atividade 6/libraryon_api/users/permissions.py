from rest_framework import permissions

from .models import *


class ReadUserOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False


class IsOwnerOfPostOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner == request.user


class IsOneProfileOfTheUserOrAccessDenied(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user in obj.profiles.all()


# class IsOwnerOfCommentOrManagerOfPost(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         else:
#             id = obj.postId
#             post = Post.objects.get(id=id.id)
#             user = User.objects.get(id=post.userId.id)
#             return request.user in user.profiles.all()




