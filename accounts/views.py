from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer,RoleUpdateSerializer,SuccessSerializer
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAdmin
from django.shortcuts import get_object_or_404
from .models import User

from drf_spectacular.utils import extend_schema
from drf_spectacular.types import OpenApiTypes



class RegisterAPIView(APIView):

    @extend_schema(
            request=RegistrationSerializer,
            responses={201:SuccessSerializer,
                       400:OpenApiTypes.OBJECT}
    )
    def post(self,request):
        serializer=RegistrationSerializer(data = request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({"message":"Registration Successful."}, status = status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    



class RoleUpdateAPIView(APIView):

    permission_classes=[IsAuthenticated,IsAdmin]

    @extend_schema(
            request=RoleUpdateSerializer,
            responses={
                200:SuccessSerializer,
                400:OpenApiTypes.OBJECT
            }
    )

    def patch(self,request,pk):

        user=get_object_or_404(
            User,
            pk = pk
        )

        serializer=RoleUpdateSerializer(
            instance = user,
            data = request.data,
            partial = True
        )
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                {"message":f"Congratulations! {user.username} is successfully an ADMIN now."},
                status = status.HTTP_200_OK
            )

        return Response( serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    




