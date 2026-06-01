from django.urls import path
from .views import RegisterAPIView,TestProtectedAPIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns=[
    
    path('register/',RegisterAPIView.as_view(),name='register'),

    path('login/',TokenObtainPairView.as_view(),name='login'),

    path('token/refresh/',TokenRefreshView.as_view()),

    path('test/',TestProtectedAPIView.as_view(),name='test-protected-api')
]