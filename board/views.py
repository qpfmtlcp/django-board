from django.shortcuts import render
from django.http import HttpResonse

def index(request):
    return HttpResonse("first app here!")