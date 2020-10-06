from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import Questionboard, AnswerBoard

class QuestionSerializer(serializers.ModelSerializer):
    
    class meta:
        model = Questionboard
        fields  = ['id', 'title', 'content', 'STATUS']
        
class QuestionDetailSerializer(serializers.ModelSerializer):
    
    class meta:
        model = Questionboard
        fields = ['id', 'title', 'content', 'STATUS', 'answer']
        
class AnswerSerializer(serializers.ModelSerializer):
    
    class meta:
        model = AnswerBoard
        fields = ['id','content','score']

class AnswerDetailSerializer(serializers.ModelSerializer):
    
    class meta:
        model = AnswerBoard
        fields = ['id','content','score']
