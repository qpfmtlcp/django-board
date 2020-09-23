from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework import serializers
from .models import NoticeBoard, Tag


class TagSerializer(serializers.ModelSerializer):
    tagname = serializers.StringRelatedField(
        # many=True, read_only=True, slug_field="tagname"
    )

    class Meta:
        model = Tag
        fields = ['tagname']


class NoticeBoardSerializer(serializers.ModelSerializer):
    tag = TagSerializer(required=False)
    title = serializers.CharField(max_length=50)
    contents = serializers.CharField(max_length=50)

    class Meta:
        model = NoticeBoard
        fields = ['id', 'title', 'contents', 'created', 'tag']

    def create(self, validated_data):
        # tagname = validated_data.get("tag")
        # print(tagname)
        # tag = Tag()
        # tag.save()
        # tag.objects.create(tagname=tagname)
        return NoticeBoard.objects.create(**validated_data)
