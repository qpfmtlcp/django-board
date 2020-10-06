
from rest_framework import generics
from django.shortcuts import render
from .models import Questionboard, AnswerBoard
from.serializer import QuestionSerializer, QuestionDetailSerializer, AnswerSerializer, AnswerDetailSerializer


# Create your views here.

class QuestionView(generics.ListCreateAPIView):
    queryset = Questionboard.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questionboard.objects.all()
    serializer_class = QuestionDetailSerializer
    
class AnswerView(generics.ListCreateAPIView):
    qeuryset = AnswerBoard.objects.all()
    serializer_class = AnswerSerializer
    
class AnswerDetailView(generics.ListCreateAPIView):
    qeuryset = AnswerBoard.objects.all()
    serializer_class = AnswerDetailSerializer