from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.board.boardList, name='boardList'),
    path('', views.board.createBoard, name='createBoard'),
    path('', views.board.deleteBoard, name='deleteBoard'),
    path('', views.board.updateBoard, name='updateBoard'),
]
