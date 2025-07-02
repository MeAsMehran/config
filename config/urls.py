"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include , re_path

# from rest_framework.authtoken.views import obtain_auth_token        # using this because of tokenAuthentication: we wanted to have a method which users enter their username and password and the token is created for that user

from rest_framework_simplejwt import views as jwt_views

# from api.views import RevokeToken

from dj_rest_auth.views import PasswordResetConfirmView
from django.views.generic import TemplateView

urlpatterns = [

    path('admin/', admin.site.urls),
    path("", include("blog.urls")),     # app blog urls
    path("api/", include("api.urls")),  # app api urls
    path('api-auth/', include('rest_framework.urls')),  # According to rest framework documentation we add this here: this is for showing api-browsable page in our website. Mostly use for sessionAuthentication

    # path('api/token-auth/', obtain_auth_token),         # this url is because of tokenAuthentication (explained above). Also you can change the url path. This view is for POST method
    # path('api/revoke/', RevokeToken.as_view(), name="revokeToken"),

    # path('api/rest-auth/', include('dj_rest_auth.urls')),       # You can change url path
    # path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path("^account-confirm-email/(?P<key>[\s\d\w().+-_',:&]+)/$", TemplateView.as_view(template_name='account _confirm.html'),name='account_confirm_email'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

] 
