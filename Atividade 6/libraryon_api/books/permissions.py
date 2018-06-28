from rest_framework import permissions

from users.models import Author


class OnlyAuthorCanCreateABook(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return Author.objects.filter(auth_profile=request.user).exists()


class IsAuthorOfBookOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if Author.objects.get(auth_profile=request.user).exists():
                author = Author.objects.get(auth_profile=request.user)
                return obj.authors.filter(auth_profile=author.auth_profile).exists()
            return False


class OnlyTheLectorWhoAssignedTheScoreCanEditIt(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.lector == request.user


class ViewBookPermissions(permissions.DjangoObjectPermissions):
    """
    Similar to `DjangoObjectPermissions`, but adding 'view' permissions.
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


# class IsOwnerOfCommentOrManagerOfPost(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         else:
#             id = obj.postId
#             post = Post.objects.get(id=id.id)
#             user = User.objects.get(id=post.userId.id)
#             return request.user in user.profiles.all()
