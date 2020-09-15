from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializer import BoardSerializer
from .models import board

class BoardView(generics.ListCreateAPIView):
    queryset = board.objects.all()
    serializer_class = BoardSerializer
    
class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = board.objects.all()
    serializer_class = BoardSerializer
