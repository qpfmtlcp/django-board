from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework import serializers
from .models import NoticeBoard, Tag, TagListRelatedBoard


class TagSerializer(serializers.ModelSerializer):
    tagname = serializers.StringRelatedField()

    class Meta:
        model = Tag
        fields = ['tagname']


class NoticeBoardSerializer(serializers.ModelSerializer):
    tag = TagSerializer(required=False, read_only=True)
    title = serializers.CharField(max_length=50)
    contents = serializers.CharField(max_length=50)

    class Meta:
        model = NoticeBoard
        fields = ['id', 'title', 'contents', 'created', 'tag']

    def create(self, validated_data):
        return NoticeBoard.objects.create(**validated_data)


class TagListRelatedBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagListRelatedBoard
        fields = ['id']
