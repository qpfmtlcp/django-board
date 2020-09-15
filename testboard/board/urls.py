from django.urls import path, include
from rest_framework import routers
from . import views

#router = routers.DefaultRouter()
#router.register(r'board', views.BoardView.as_view())
#router.register(r'board/<int:pk>',  views.BoardDetail.as_view())


urlpatterns = [
    #path('', include(router.urls)),
    path('board/', views.BoardView.as_view()),
    path('board/<int:pk>/', views.BoardDetail.as_view()),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('', views.Board.boardList, name='boardList'),
    #path('', views.Board.createBoard, name='createBoard'),
    #path('', views.Board.deleteBoard, name='deleteBoard'),
    #path('', views.Board.updateBoard, name='updateBoard'),
]
