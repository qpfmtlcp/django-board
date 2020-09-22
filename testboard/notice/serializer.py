from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework import serializers
from .models import NoticeBoard, Tag


class TagSerializer(serializers.ModelSerializer):
    tag = Tag.StringRelatedField()

    class Meta:
        model = Tag
        fields = ['tagname']


class NoticeBoardSerializer(serializers.ModelSerializer):
    tag = TagSerializer(max_length=50, required=False)
    title = serializers.CharField(max_length=50)
    contents = serializers.CharField(max_length=50)

    class Meta:
        model = NoticeBoard
        fields = ['id', 'title', 'contents', 'created', 'tag']

    def create(self, validated_data):
        tagname = validated_data.get("tag")
        tag = Tag.objects.get(tagname=tagname)
        if tag is None:
            raise serializers.ValidationError('tag is not exist.')

        return NoticeBoard.objects.create(**validated_data)
