from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import generics
from .serializer import BoardSerializer
from .models import board

#django restframework 설치 (generic view와 seriealizer를 사용하기 위해서)
#기본 CRUD API 생성
#To-do: 제네릭뷰 사용   
class BoardViewSet(viewsets.ModelViewSet):
    queryset = board.objects.all()
    serializer_class = BoardSerializer

'''
# CRUD view 
class Board:
    def boardList(self, request):
        list = board.objects.all()
        return render(request, 'main.html',{'boardList': list})

    def createBoard(self, request):
        return render(request, 'main.html')

    def deleteBoard(self, request):
        return render(request, 'main.html')
    
    def updateBoard(self, request):
        return render(request, 'main.html')

'''

