from .models import Board, User, History
from rest_framework import serializers

class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    history = serializers.StringRelatedField(many=True)
    class Meta:
        model = Board
        fields = ['title', 'status', 'contents', 'created', 'modified', 'owner','history']

class UserSerializer(serializers.ModelSerializer):
    #title =  serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ['username']

class HistorySerializer(serializers.ModelSerializer):
    currentUser = serializers.StringRelatedField()
    modifiedDate = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='modified')
    
    class Meta:
        model = History
        fields = ['currentUser','modifiedDate']
