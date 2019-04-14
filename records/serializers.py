from django.contrib.auth.models import User
from rest_framework import serializers
from records.models import Record


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Record
        fields = ('url', 'id', 'owner', 'title', 'code', 'language',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    records = serializers.HyperlinkedRelatedField(many=True, view_name='record-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'records')
