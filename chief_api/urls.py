"""
chief_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.schemas import get_schema_view
from records import views

schema_view = get_schema_view(title='Chief API')

urlpatterns = [
    path('', include('records.urls')),
    path('auth/', include('authentication.urls')),

    path('admin/', admin.site.urls), # Django Admin
    path('api-auth/', include('rest_framework.urls')), # DRF Login

    path('schema/', schema_view),
]
