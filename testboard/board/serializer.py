from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework import serializers
from .models import Board, History, Tag



class TagSerializer(serializers.ModelSerializer):
    tagname = serializers.StringRelatedField()
    #board = BoardSerializer(many=True, read_only=True)
    
    class Meta:
        model = Tag
        fields = '__all__' 
                
class TagRetriveSerializer(serializers.ModelSerializer):
    tagname = serializers.StringRelatedField()
    #slug = serializers.SlugField(max_length=50, min_length=None, allow_blank=False)
    board = Board.objects.filter(tag = Tag.objects.filter(tagname = tagname))
    
    class Meta:
        model = Tag
        fields = ['tagname','board']
            
class HistorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = History
        fields = ['user', 'created']


class BoardCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50, required=False)
    contents = serializers.CharField(max_length=50, required=False)
    tag = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Board
        fields = [
            'id',
            'title',
            'contents',
            'image',
            'tag',
        ]

    def create(self, validated_data):
        title = validated_data.get("title")
        contents = validated_data.get("contents")
        if title is None:
            raise serializers.ValidationError('title is not exist.')
        
        if Board.objects.filter(title=title):
            raise serializers.ValidationError('title is already exist. put another title name')
    
        if contents is None:
            raise serializers.ValidationError('contents is not exist.')
        
        user = self.context['request'].user
        return Board.objects.create(owner=user, **validated_data)


class BoardSerializer(serializers.ModelSerializer):
    history = HistorySerializer(many=True, read_only=True)
    title = serializers.CharField(max_length=50, required=False)
    contents = serializers.CharField(max_length=50, required=False)
    STATUS = ('draft', 'published')
    status = serializers.ChoiceField(STATUS)
    tag = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Board
        fields = [
            'title',
            'status',
            'contents',
            'created',
            'modified',
            'history',
            'tag'
        ]

    def update(self, instance, validated_data):
        if get_user_model().objects.filter(username="siransfe").exists() == True:
            History.objects.create(
                board=instance, user=get_user_model().objects.get(username="siransfe")
            )
        else:
            raise serializers.ValidationError("user is not valid")
        instance.status = validated_data.get('status', instance.status)
        instance.title = validated_data.get('title', instance.title)
        instance.contents = validated_data.get('contents', instance.contents)
        instance.save()
        return instance
