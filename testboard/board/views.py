from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello world!")

#기본 CRUD API 생성 create replace update delete 하는 view 생성.
#제네릭뷰를 사용하자고 함. 
