from rest_framework import renderers, viewsets
from rest_framework.decorators import action, api_view
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.models import User

from records.models import Record
from records.serializers import RecordSerializer, UserSerializer
from records.permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def auth_api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'owners': reverse('owner-list', request=request, format=format),
        'collaborators': reverse('collaborator-list', request=request, format=format),
        'readers': reverse('reader-list', request=request, format=format),
    })


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
