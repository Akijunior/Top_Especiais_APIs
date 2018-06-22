from django.urls import path

from books import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name=views.BookList.name),
    path('books/<int:pk>', views.BookDetail.as_view(), name=views.BookDetail.name),
    path('genres/', views.GenreList.as_view(), name=views.GenreList.name),
    path('genres/<int:pk>', views.GenreDetail.as_view(), name=views.GenreDetail.name),
]