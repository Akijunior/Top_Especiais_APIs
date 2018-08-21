from django.urls import path, include

from . import views

urlpatterns = [
    
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    
    path('authors/', views.AuthorList.as_view(), name=views.AuthorList.name),
    path('authors/<int:pk>', views.AuthorDetail.as_view(), name=views.AuthorDetail.name),
    path('authors/create/', views.AuthorCreate.as_view(), name=views.AuthorCreate.name),

    path('lectors/', views.LectorList.as_view(), name=views.LectorList.name),
    path('lectors/<int:pk>', views.LectorDetail.as_view(), name=views.LectorDetail.name),
    path('lectors/create/', views.LectorCreate.as_view(), name=views.LectorCreate.name),

    path('users/', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
]