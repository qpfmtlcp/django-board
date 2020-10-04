from rest_framework import generics
from rest_framework import permissions

from django_filters import rest_framework as filters

from .serializer import (
    BoardSerializer,
    BoardCreateSerializer,
    HistorySerializer,
)
from .models import Board, History


class BoardFilter(filters.FilterSet):
    class Meta:
        model = Board
        fields = [
            'status',
            'owner',
        ]


'''
class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ['username']'''


class BoardView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = BoardFilter


class BoardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class HistoryView(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
