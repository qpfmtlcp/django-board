from django.urls import path

from . import views

urlpatterns = [
    path('board/', views.BoardView.as_view()),
    path('board/<int:pk>/', views.BoardDetailView.as_view()),
    path('history/', views.HistoryView.as_view()),
    path('tag/', views.TagView.as_view()),
    path('tag/<str:tagname>/', views.TagDetailView.as_view())
]