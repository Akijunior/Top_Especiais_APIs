from django.urls import path, include

from user import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('comments', views.CommentViewSet)
router.register('posts', views.PostViewSet)

app_name='user'
urlpatterns = [
    # path('users/<int:user_id>/posts/<int:post_id>', views.user_post_detail),
    path('', include(router.urls)),
]
#
# urlpatterns = [
#     path('users/', views.UserOperations.as_view(),
#          name='user-list'),
#     path('users/<int:id>/', views.UserDetail.as_view(),
#          name='user-detail'),
#     path('comments/', views.CommentOperations.as_view(),
#          name='comment-list'),
#     path('comments/<int:pk>/', views.CommentOperations.as_view(),
#          name='comment-detail'),
#     path('posts/', views.PostOperations.as_view(),
#          name='post-list'),
#     path('posts/<int:pk>/', views.PostOperations.as_view(),
#          name='post-detail'),
#     path('', views.ApiRoot.as_view(),
#          name=views.ApiRoot.name),
#     # path('', index, name='index'),
# ]
