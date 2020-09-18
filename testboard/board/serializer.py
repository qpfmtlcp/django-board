from .models import Board, User, History
from rest_framework import serializers


class HistorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = History
        fields = ['user', 'created']


class BoardSerializer(serializers.ModelSerializer):
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
            'history',
            'user',
        ]

    def update(self, instance, validated_data):
        username = validated_data.pop("user")
        checkUser = User.objects.filter(username=username)
        if checkUser.exists():
            currentUser = User.objects.get(username=username)
            History.objects.create(board=instance, user=currentUser)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
