from .models import Board, User
from rest_framework import serializers

class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    class Meta:
        model = Board
        fields = ['title', 'status', 'contents', 'created', 'modified', 'owner']

class UserSerializer(serializers.ModelSerializer):
    #title =  serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ['username']
