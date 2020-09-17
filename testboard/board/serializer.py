from .models import Board, User, History
from rest_framework import serializers


class HistorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = History
        fields = ['user', 'created']


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

    def update(self, instance, validated_data):
        username = validated_data.pop("user")
        currentUser = User.objects.all()
        for name in currentUser:
            if name.username == username:
                print(name.id)
                History.objects.create(user=currentUser)
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
