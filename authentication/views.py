from django.shortcuts import render
from django.conf import settings


from django.contrib.auth.models import User
from authentication.models import Owner, Collaborator, Reader, GithubUser
from authentication.serializers import UserSerializer, OwnerSerializer, CollaboratorSerializer, ReaderSerializer, GithubUserSerializer


import requests
import os
import json
from django.core.exceptions import ImproperlyConfigured


from rest_framework import generics, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.settings import api_settings


with open(os.path.abspath("./secrets.json")) as f:
    secrets = json.loads(f.read())


# TODO This should be some sort of service
def get_secret_setting(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))


class AuthViewSet(viewsets.ViewSet):
    """
    This viewset implements the convert_token method for getting an access token, as well as the get_github_self method for returning the current user's basic Github data.
    """

    @action(detail=False, methods=['POST'], renderer_classes=[renderers.JSONRenderer,])
    def convert_token(self, request, *args, **kwargs):
        """
        This method takes the `access_code` passed to it from the front end, and makes a POST request to https://github.com/login/oauth/access_token, which then returns an authorization_token for further requests.
        """
        # print(request.data.code)
        r = requests.post("https://github.com/login/oauth/access_token", data = {
            'code': request.data['code'],
            'client_id': get_secret_setting('SOCIAL_AUTH_GITHUB_KEY'),
            'client_secret': get_secret_setting('SOCIAL_AUTH_GITHUB_SECRET'),
            'redirect_uri': "http://localhost:3000/callback",
            'state': "This State is a Test State",
        })
        key_value_pairs = r.text.split("&")
        data = {}
        for key_value_string in key_value_pairs:
            split = key_value_string.split("=")
            data[split[0]] = split[1]
        # TODO Use proper HTTP status codes
        return Response({
            'data': data,
            'status_code': 200,
        })

    @action(detail=False, methods=['GET'], renderer_classes=[renderers.JSONRenderer,])
    def get_github_self(self, request, *args, **kwargs):
        """
        This method returns the user profile associated with the current `authorization_token` from GitHub, i.e. the user currently logged in.
        """
        print("hit get_github_self")
        print(request.headers['Authorization'])
        headers = {
            'Authorization': str(request.headers['Authorization']),
        }
        r = requests.get("https://api.github.com/user", headers=headers)
        print(r)
        print(r.text)
        return Response({
            'data': json.loads(r.text),
            'status_code': 200,
        })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides actions:
        list
        details
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class CollaboratorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
