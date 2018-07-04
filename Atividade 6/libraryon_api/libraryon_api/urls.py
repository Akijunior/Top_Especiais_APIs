from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from libraryon_api.oauth_token import exchange_token
from users.views import CustomAuthToken
schema_view = get_swagger_view(title='Libraryon API Library')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('users.urls'), name='users'),
    path('', include('books.urls'), name='books'),
    path('docs/', schema_view),


    ##    Authentication Paths    ##		

    ## Session
	path('api-auth/', include('rest_framework.urls')),

	## Token
	path('api/token/custom', CustomAuthToken.as_view(), name=CustomAuthToken.name),

    ## OAuth
    path('o/', include('rest_framework_social_oauth2.urls')),
    path('social/<backend>/', exchange_token),

    ## JWT 
    path('api/token/jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

