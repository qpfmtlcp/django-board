
from rest_framework import generics
from django.shortcuts import render
from .models import Questionboard, AnswerBoard
from.serializer import QuestionSerializer, QuestionDetailSerializer


# Create your views here.

class QuestionView(generics.ListCreateAPIView):
    queryset = Questionboard.objects.all()

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questionboard.objects.all()
    
class AnswerView(generics.ListCreateAPIView):
    qeuryset = AnswerBoard.objects.all()
    
class AnswerDetailView(generics.ListCreateAPIView):
    qeuryset = AnswerBoard.objects.all()