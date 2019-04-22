from rest_framework import serializers
from authentication.models import Owner, Collaborator, Reader, GithubUser
from django.contrib.auth.models import User
from records.serializers import RecordSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='owner-detail', read_only=True)
    collaborator = serializers.HyperlinkedRelatedField(many=False, view_name='collaborator-detail', read_only=True)
    reader = serializers.HyperlinkedRelatedField(many=False, view_name='reader-detail', read_only=True)
    github_user = serializers.HyperlinkedRelatedField(many=False, view_name='githubuser-detail', read_only=True)
    records = serializers.HyperlinkedRelatedField(many=True, view_name='record-detail', read_only=True)

    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'username',
            'owner',
            'collaborator',
            'reader',
            'github_user',
            'records',
        )


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    records = RecordSerializer(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = (
            'url',
            'id',
            'user',
            'records',
        )


class CollaboratorSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    records = RecordSerializer(many=True, read_only=True)

    class Meta:
        model = Collaborator
        fields = (
            'url',
            'id',
            'user',
            'records',
        )

class ReaderSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    records = RecordSerializer(many=True, read_only=True)

    class Meta:
        model = Reader
        fields = (
            'url',
            'id',
            'user',
            'records',
        )


class GithubUserSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    
    class Meta:
        model = GithubUser
        fields = (
            'url',
            'id',
            'created',
        )