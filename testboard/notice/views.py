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
from .serializer import (
    NoticeBoardSerializer,
    TagSerializer,
    TagListRelatedBoardSerializer,
)
from .models import NoticeBoard, Tag, TagListRelatedBoard


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


class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagListRelatedBoardView(generics.ListCreateAPIView):
    queryset = TagListRelatedBoard.objects.all()
    serializer_class = TagListRelatedBoardSerializer