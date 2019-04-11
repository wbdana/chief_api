from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from social_django.models import UserSocialAuth

# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None
