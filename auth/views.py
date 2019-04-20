from django.shortcuts import render
from django.conf import settings
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
    This viewset implements the get_github_access_code method for basic GitHub authentication.
    """

    # @action(detail=True, renderer_classes=[renderers.JSONRenderer, renderers.StaticHTMLRenderer,])
    # def get_github_access_code(self, request, *args, **kwargs):
    #     print(request)
    #     params = {
    #         'client_id': get_secret_setting('SOCIAL_AUTH_GITHUB_KEY'),
    #         'scope': 'repo gist',
    #         'redirect_uri': settings.LOGIN_REDIRECT_URL
    #     }
    #     r = requests.get('https://github.com/login/oauth/authorize', params=params)
    #     print(r.status_code)
    #     print(r)
    #     # print(r.text)
    #     # print(r.json())
    #     return Response(r.text)

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
        print("STATUS CODE " + str(r.status_code))
        print(r.text)

        # TODO This method should really process the data itself for the front end
        key_value_pairs = r.text.split("&")
        data = {}
        for key_value_string in key_value_pairs:
            split = key_value_string.split("=")
            data[split[0]] = split[1]
        print("did it work?")
        
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
            'success': "OH YEAH",
            'status_code': 200,
        })




