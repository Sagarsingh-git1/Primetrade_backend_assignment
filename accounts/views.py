from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class RegisterAPIView(APIView):
    
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({"message":"Registration Successful."},status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class TestProtectedAPIView(APIView):

    permission_classes=[IsAuthenticated]
    
    def get(self,request):

        return Response({"message":f"Welcome! {request.user.username}"})
    
    


    