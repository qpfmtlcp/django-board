from rest_framework import generics

from django_filters import rest_framework as filters

from .serializer import (
    BoardSerializer,
    BoardCreateSerializer,
    UserSerializer,
    HistorySerializer,
)
from .models import Board, User, History


class BoardFilter(filters.FilterSet):
    class Meta:
        model = Board
        fields = [
            'status',
            'owner',
        ]


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ['username']


class BoardView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer
    filterset_class = BoardFilter


class BoardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HistoryView(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
