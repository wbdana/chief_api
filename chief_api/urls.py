"""chief_api URL Configuration

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
# from django.contrib.auth.views import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from records import views

urlpatterns = [
    path('admin/', admin.site.urls), # Django Admin
    path('api-auth/', include('rest_framework.urls')), # DRF Login
    path('auth/', include('rest_framework_social_oauth2.urls')), # Social OAuth2

    path('', include('records.urls')),

    # path('login/', LoginView, name='login'),
    # path('logout/', LogoutView, name='logout'),

    # path('oauth/', include('social_django.urls', namespace='social')),

    # path('settings/', views.settings, name='settings'),
    # path('settings/password/', views.password, name='password'),

    # path('api-auth/', include('rest_framework.urls')),
]
