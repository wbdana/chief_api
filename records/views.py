from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm

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
    
    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
    
    return render(request, 'settings.html', {
        'github_login': github_login,
        'can_disconnect': can_disconnect
    })


def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm
    
    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully changed.')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'password.html', {'form': form})