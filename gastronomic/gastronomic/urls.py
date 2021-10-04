"""gastronomic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from users.views import activate, activateRe
from graphene_file_upload.django import FileUploadGraphQLView

from graphql_jwt.decorators import jwt_cookie

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('graphql/', FileUploadGraphQLView.as_view(graphiql=True)),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('activate/<uidb64>/<token>',activate, name='activate'),
    path('activateRe/<uidb64>/<token>',activateRe, name='activateRe'),
    path("graphql/", jwt_cookie(GraphQLView.as_view())),
]
