from .models import Board
from rest_framework import serializers

class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'status', 'contents', 'created', 'modified']
