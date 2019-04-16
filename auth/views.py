from django.shortcuts import render
from django.conf import settings
import requests

import os
import json
from django.core.exceptions import ImproperlyConfigured


from rest_framework import generics, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


with open(os.path.abspath("./secrets.json")) as f:
    secrets = json.loads(f.read())


def get_secret_setting(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))



class AuthViewSet(viewsets.GenericViewSet):
    """
    This viewset implements the get_github_user_identity method for basic GitHub authentication.
    """

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer,])
    def get_github_user_identity(self, request, *args, **kwargs):
        print(request)
        params = {
            'client_id': get_secret_setting('SOCIAL_AUTH_GITHUB_KEY'),
            'scope': 'repo gist',
            'redirect_uri': settings.LOGIN_REDIRECT_URL
        }
        r = requests.get('https://github.com/login/oauth/authorize', params=params)
        print(r.status_code)
        print(r)
        # print(r.text)
        # print(r.json())
        return Response(r.text)


