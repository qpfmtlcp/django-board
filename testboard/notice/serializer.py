from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework import serializers
from .models import NoticeBoard


class NoticeBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeBoard
        fields = ['id', 'contents', 'created']
