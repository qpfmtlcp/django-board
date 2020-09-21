from django.urls import path

from . import views

urlpatterns = [
    path('noticeboard/', views.NoticeBoardView.as_view()),
    path('noticeboard/<int:pk>/', views.NoticeBoardDetailView.as_view()),
]
