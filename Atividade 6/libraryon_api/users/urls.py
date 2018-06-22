from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('api-auth/', include('rest_framework.urls')),

    path('authors/', views.AuthorList.as_view(), name=views.AuthorList.name),
    path('authors/<int:pk>', views.AuthorDetail.as_view(), name=views.AuthorDetail.name),
    path('lectors/', views.LectorList.as_view(), name=views.LectorList.name),
    path('lectors/<int:pk>', views.LectorDetail.as_view(), name=views.LectorDetail.name),
]