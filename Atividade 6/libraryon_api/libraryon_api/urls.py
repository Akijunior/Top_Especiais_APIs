from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls'), name='users'),
    path('', include('books.urls'), name='books'),
    path('docs/', include_docs_urls(title='Libraryon API Library', public=False)),
]
