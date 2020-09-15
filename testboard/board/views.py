from django.shortcuts import render
from django.http import HttpResponse
#from rest_framework import generics
#from .serializer import BoardSerializer
from .models import board
#To-do: template 생성, 연결 

# CRUD view 
class board:
    def boardList(self, request):
        list = board.objects.all()
        return render(request, 'main.html',{'boardList': list})

    def createBoard(self, request):
        return render(request, 'main.html')

    def deleteBoard(self, request):
        return render(request, 'main.html')
    
    def updateBoard(self, request):
        return render(request, 'main.html')
    



#django restframework 설치 (generic view와 seriealizer를 사용하기 위해서)
#기본 CRUD API 생성
#제네릭뷰 사용 필요
'''
class BoardList(generics.ListAPIView):
    queryset = board.objects.all()
    serializer_class = BoardSerializer
    '''



