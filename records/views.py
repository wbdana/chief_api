from rest_framework import renderers, viewsets
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response

from django.contrib.auth.models import User

from records.models import Record
from records.serializers import RecordSerializer, UserSerializer
from records.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides actions:
        list
        details
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RecordViewSet(viewsets.ModelViewSet):
    """
    Provides actions:
        list
        create
        retrieve
        update
        destroy
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)





# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm

# from social_django.models import UserSocialAuth

# Create your views here.

# @login_required
# def index(request):
#     return render(request, 'index.html')


# def login(request):
#     return render(request, 'login.html')


# def settings(request):
#     user = request.user

#     try:
#         github_login = user.social_auth.get(provider='github')
#     except UserSocialAuth.DoesNotExist:
#         github_login = None
    
#     can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
    
#     return render(request, 'settings.html', {
#         'github_login': github_login,
#         'can_disconnect': can_disconnect
#     })


# def password(request):
#     if request.user.has_usable_password():
#         PasswordForm = PasswordChangeForm
#     else:
#         PasswordForm = AdminPasswordChangeForm
    
#     if request.method == 'POST':
#         form = PasswordForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request, 'Your password was successfully changed.')
#             return redirect('password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordForm(request.user)
#     return render(request, 'password.html', {'form': form})