from django.shortcuts import render
from django.http import HttpResponse
#from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from .serializer import BoardSerializer
from .models import board

#django restframework 설치 (generic view와 seriealizer를 사용하기 위해서)
#기본 CRUD API 생성
#To-do: 제네릭뷰 사용
'''
class BoardViewSet(viewsets.ModelViewSet):
    queryset = board.objects.all()
    serializer_class = BoardSerializer
'''
'''
class BoardViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = board.objects.all()
    serializer_class = BoardSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
'''
class BoardView(generics.ListCreateAPIView):
    queryset = board.objects.all()
    serializer_class = BoardSerializer
    
class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = board.objects.all()
    serializer_class = BoardSerializer  
