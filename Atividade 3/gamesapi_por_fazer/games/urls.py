"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.urls import path

from games import views

urlpatterns = [
    path('games/', views.GameOperations.as_view(),
         name='game-list'),
    path('games/<int:pk>/', views.GameOperations.as_view(),
         name='game-detail'),
    path('game-categories/', views.GameCategoryOperations.as_view(),
         name='game-category-list'),
    path('game-categories/<int:pk>/', views.GameCategoryOperations.as_view(),
         name='game-category-detail'),
    path('players/', views.PlayerOperations.as_view(),
         name='player-list'),
    path('players/<int:pk>/', views.PlayerOperations.as_view(),
         name='player-detail'),
    path('scores/', views.ScoreOperations.as_view(),
         name='score-list'),
    path('scores/<int:pk>/', views.ScoreOperations.as_view(),
         name='score-detail'),
    path('', views.ApiRoot.as_view(),
         name=views.ApiRoot.name),
]
