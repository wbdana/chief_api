from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.schemas import get_schema_view
from authentication import views


authentication_router = SimpleRouter()
authentication_router.register(r'owners', views.OwnerViewSet)
authentication_router.register(r'collaborators', views.CollaboratorViewSet)
authentication_router.register(r'readers', views.ReaderViewSet)
authentication_router.register(r'users', views.UserViewSet)
authentication_router.register(r'auth', views.AuthViewSet, base_name='auth')
