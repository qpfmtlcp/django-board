from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework import serializers
from .models import NoticeBoard, Tag


class TagSerializer(serializers.ModelSerializer):
    tagname = serializers.StringRelatedField()

    class Meta:
        model = Tag
        fields = ['pk', 'tagname']


class NoticeBoardSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True, read_only=True)
    title = serializers.CharField(max_length=50)
    contents = serializers.CharField(max_length=50)

    class Meta:
        model = NoticeBoard
        fields = ['id', 'title', 'contents', 'created', 'tag']

    def create(self, validated_data):
        obj = super().create(validated_data)
        print(obj)
        tag = Tag.objects.create(tagname="siran")
        notice = NoticeBoard.objects.create(**validated_data)
        notice.tag.add(tag)
        return notice
