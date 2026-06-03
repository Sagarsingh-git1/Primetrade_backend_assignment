from django.urls import path
from .views import RegisterAPIView,RoleUpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns=[
    
    path('register/',RegisterAPIView.as_view(),name='register'),

    path('login/',TokenObtainPairView.as_view(),name='login'),

    path('token/refresh/',TokenRefreshView.as_view()),

    path('role/<int:pk>/',RoleUpdateAPIView.as_view(), name='role-update')
]