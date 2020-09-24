from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework import serializers
from .models import Board, History


class HistorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = History
        fields = ['user', 'created']


class BoardCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50, required=False)
    contents = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = Board
        fields = [
            'id',
            'title',
            'contents',
        ]

    def create(self, validated_data):
        title = validated_data.get("title")
        contents = validated_data.get("contents")
        if title is None:
            raise serializers.ValidationError('title is not exist.')

        if contents is None:
            raise serializers.ValidationError('contents is not exist.')
        user = get_user_model().objects.get(username="siransfe")
        return Board.objects.create(owner=user, **validated_data)


class BoardSerializer(serializers.ModelSerializer):
    history = HistorySerializer(many=True, read_only=True)
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
        ]

    def update(self, instance, validated_data):
        if get_user_model().objects.filter(username="siransfe").exists() == True:
            History.objects.create(
                board=instance, user=get_user_model().objects.get(username="siransfe")
            )
        else:
            raise serializers.ValidationError("user is not valid")
        instance.status = validated_data.get('status', instance.status)
        instance.title = validated_data.get('title', instance.title)
        instance.contents = validated_data.get('contents', instance.contents)
        instance.save()
        return instance
