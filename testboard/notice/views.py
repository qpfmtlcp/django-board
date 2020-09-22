from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    SAFE_METHODS,
    IsAdminUser,
)
from django_filters import rest_framework as filters
from .serializer import NoticeBoardSerializer
from .models import NoticeBoard


class NoticeBoardView(generics.ListCreateAPIView):
    queryset = NoticeBoard.objects.all()
    serializer_class = NoticeBoardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoticeBoardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoticeBoard.objects.all()
    serializer_class = NoticeBoardSerializer
    permission_classes = [IsAuthenticated]
