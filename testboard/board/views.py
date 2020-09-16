from rest_framework import generics
from .serializer import BoardSerializer
from django_filters import rest_framework as filters
from .models import Board


class BoardFilter(filters.FilterSet):
    class Meta:
        model = Board
        fields = ['status']
        
class BoardView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filterset_class= BoardFilter

    
class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
