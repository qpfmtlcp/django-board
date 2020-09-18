from .models import Board, User, History
from rest_framework import serializers


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['board', 'created']


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    history = HistorySerializer(many=True, read_only=True)
    user = serializers.CharField(max_length=30, write_only=True)

    class Meta:
        model = Board
        fields = [
            'title',
            'status',
            'contents',
            'created',
            'modified',
            'owner',
            'history',
            'user',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
