from rest_framework import renderers, viewsets
from rest_framework.decorators import action, api_view
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.models import User

from records.models import Record
from records.serializers import RecordSerializer, UserSerializer
from records.permissions import IsOwnerOrReadOnly


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
