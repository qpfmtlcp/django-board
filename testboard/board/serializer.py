from .models import board
from rest_framework import serializers

#model seriealizer 대신 hyperlinkedModelSerializer를 사용
#차이점
#It does not include the id field by default. id 필드가 필요 없음
#It includes a url field, using HyperlinkedIdentityField.
#Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.

class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = board
        #fields = ('draft','published')
        fields = ['title', 'contents', 'created', 'modified']