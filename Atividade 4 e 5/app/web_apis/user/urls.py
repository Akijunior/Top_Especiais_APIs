from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name='user'
urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('api-auth/', include('rest_framework.urls')),

    path('users/', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('posts/', views.PostList.as_view(), name=views.PostList.name),
    path('posts/<int:pk>', views.PostDetail.as_view(), name=views.PostDetail.name),
    path('comments/', views.CommentList.as_view(), name=views.CommentList.name),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name=views.CommentDetail.name),


    path('users/<int:user_id>/posts/', views.UserDetail.as_view(), name='user-posts'),
    path('users/<int:pk>/posts/<int:post_id>', views.UserPostDetail.as_view(), name='user-post-detail'),
    path('users/<int:pk>/posts/<int:post_id>/comments/', views.UserPostComments.as_view(), name='user-post-comment'),
    path('users/<int:pk>/posts/<int:post_id>/comments/<int:comment_id>', views.UserPostCommentDetail.as_view(), name='user-post-comment-detail'),

    path('api-token-auth/', obtain_auth_token),
    path('api-token-auth2/', views.CustomAuthToken.as_view()),

]

# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('users', views.UserViewSet)
# router.register('comments', views.CommentViewSet)
# router.register('posts', views.PostViewSet)
# router.register('related-user', views.UserRelatedViewSet)
# router.register('user-posts', views.PostHyperViewSet)
# router.register('users/<int:user_id>/posts/<int:post_id>', views.user_post_detail)

#
# urlpatterns = [
# path('users/<int:user_id>/posts/<int:post_id>', views.user_post_detail, name='user-post-detail'),
# path('users/<int:pk>/highlight/', views.PostHighlight.as_view()),
# path('users/<int:user_id>/posts/', views.UserPostListViewSet.as_view({'get': 'list'})),
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

