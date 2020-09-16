from django.urls import path
from . import views

urlpatterns = [
    path('board/', views.BoardView.as_view()),
    path('board/<int:pk>/', views.BoardDetailView.as_view()),
    path('user/', views.UserView.as_view()),
    path('user/<int:pk/', views.UserDetailView.as_view()),
]
