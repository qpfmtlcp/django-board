from rest_framework import generics

from django_filters import rest_framework as filters


from .models import NoticeBoard


'''class NoticeBoardFilter(filters.FilterSet):
    class Meta:
        model = Board
        fields = [
            'status',
            'owner',
        ]'''


class NoticeBoardView(generics.ListCreateAPIView):
    queryset = NoticeBoard.objects.all()
    # serializer_class = BoardCreateSerializer
    # filterset_class = BoardFilter


class NoticeBoardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoticeBoard.objects.all()
    # serializer_class = BoardSerializer
