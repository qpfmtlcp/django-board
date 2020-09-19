from .models import Board, User, History
from rest_framework import serializers
from django.core.exceptions import ValidationError


class HistorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = History
        fields = ['user', 'created']


class BoardCreateSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=30, write_only=True)
    title = serializers.CharField(max_length=50, required=False)
    contents = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = Board
        fields = [
            'id',
            'title',
            'contents',
            'user',
        ]

    def create(self, validated_data):
        user = validated_data.pop("user")
        title = validated_data.get("title")
        contents = validated_data.get("contents")
        if title is None:
            raise serializers.ValidationError('title is not exist.')

        if contents is None:
            raise serializers.ValidationError('contents is not exist.')

        if User.objects.filter(username=user).exists() == True:
            owner = User.objects.get(username=user)

        else:
            raise serializers.ValidationError('user name is not exist.')

        return Board.objects.create(owner=owner, **validated_data)


class BoardSerializer(serializers.ModelSerializer):
    history = HistorySerializer(many=True, read_only=True)
    user = serializers.CharField(max_length=30, write_only=True)
    title = serializers.CharField(max_length=50, required=False)
    contents = serializers.CharField(max_length=50, required=False)
    STATUS = ('draft', 'published')
    status = serializers.ChoiceField(STATUS)

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

    def update(self, instance, validated_data):
        username = validated_data.pop("user")
        if User.objects.filter(username=username).exists() == True:
            History.objects.create(
                board=instance, user=User.objects.get(username=username)
            )
        else:
            raise serializers.ValidationError('user name is not exist.')

        instance.status = validated_data.get('status', instance.status)
        instance.title = validated_data.get('title', instance.title)
        instance.contents = validated_data.get('contents', instance.contents)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
