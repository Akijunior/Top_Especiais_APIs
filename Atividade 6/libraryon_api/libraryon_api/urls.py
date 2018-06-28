from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Libraryon API Library')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls'), name='users'),
    path('', include('books.urls'), name='books'),
    path('docs/', schema_view),
    # path('docs/', include_docs_urls(title='Libraryon API Library', public=False)),
]

