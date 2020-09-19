from .models import Board, User, History
from rest_framework import serializers
from django.core.exceptions import ValidationError


class HistorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = History
        fields = ['user', 'created']


class BoardSerializer(serializers.ModelSerializer):
    history = HistorySerializer(many=True, read_only=True)
    user = serializers.CharField(max_length=30, write_only=True, default="")
    title = serializers.CharField(max_length=50, default="")
    contents = serializers.CharField(max_length=50, default="")

    class Meta:
        model = Board
        fields = [
            'title',
            'status',
            'contents',
            'created',
            'modified',
            'history',
            'user',
        ]

    def create(self, validated_data):
        user = validated_data.pop("user")
        checkUser = User.objects.filter(username=user)
        if checkUser.exists():
            owner = User.objects.get(username=user)
        else:
            raise serializers.ValidationError('user name is not exist.')

        board = Board.objects.create(owner=owner, **validated_data)
        return board

    def update(self, instance, validated_data):
        username = validated_data.pop("user")
        checkUser = User.objects.filter(username=username)
        if checkUser.exists():
            currentUser = User.objects.get(username=username)
            History.objects.create(board=instance, user=currentUser)
        else:
            raise serializers.ValidationError('user name is not exist.')

        title = validated_data.pop("title")
        contents = validated_data.pop("contents")
        if title:
            instance.title = title

        if contents:
            instance.contents = contents

        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
