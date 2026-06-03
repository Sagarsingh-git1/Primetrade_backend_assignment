from django.urls import path
from .views import TaskListCreateAPIView,TaskDetailAPIView



urlpatterns=[

    path('fetch_or_create/',TaskListCreateAPIView.as_view(),name='fetch-create-tasks'),

    path('fetch_create_update/<int:pk>/',TaskDetailAPIView.as_view(),name='fetch-create-update-tasks'),


]