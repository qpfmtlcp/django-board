from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'board', views.BoardViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('', views.Board.boardList, name='boardList'),
    #path('', views.Board.createBoard, name='createBoard'),
    #path('', views.Board.deleteBoard, name='deleteBoard'),
    #path('', views.Board.updateBoard, name='updateBoard'),
]
