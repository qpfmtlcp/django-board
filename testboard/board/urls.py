from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('board/', views.BoardView.as_view()),
    path('board/<int:pk>/', views.BoardDetail.as_view()),
]
