from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls'), name='user'),
    path('', include('books.urls'), name='user'),
]
