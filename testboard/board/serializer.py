from .models import board
from rest_framework import serializers

class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = board
        fields = ['title', 'contents', 'created', 'modified']