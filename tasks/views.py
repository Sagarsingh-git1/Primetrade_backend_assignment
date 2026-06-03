
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema


from .models import Task
from .serializers import TaskSerializer
from accounts.serializers import SuccessSerializer


class TaskListCreateAPIView(APIView):

    permission_classes=[IsAuthenticated]

    @extend_schema(
            request=TaskSerializer,
            responses={200:TaskSerializer(many = True)}
    )
    def get(self, request):

        if request.user.role == "ADMIN":

            tasks=Task.objects.all()
        
        else:
            
            tasks = Task.objects.filter(
                executer=request.user
            )

        serializer = TaskSerializer(tasks,many=True)

        return Response(serializer.data, status = status.HTTP_200_OK)
    

    
    @extend_schema(
            request=TaskSerializer,
            responses={
                201:SuccessSerializer,
                400:OpenApiTypes.OBJECT
            }
    )
    
    def post(self, request):

        serializer=TaskSerializer(data = request.data)

        if serializer.is_valid():

            serializer.save(executer = request.user)

            return Response({"message":"Data inserted successfully."}, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    



class TaskDetailAPIView(APIView):
    
    permission_classes=[IsAuthenticated]

    def get_object(self, pk, user):

        if user.role == "ADMIN":
            return get_object_or_404(Task , pk = pk)

        return get_object_or_404( Task , pk = pk , executer = user )
    

    @extend_schema(
            request=TaskSerializer,
            responses={200:TaskSerializer}
    )
    def get(self, request, pk):

        task=self.get_object(
            pk,
            request.user
        )

        serializer=TaskSerializer(task)

        return Response(serializer.data, status = status.HTTP_200_OK)
    
    
    @extend_schema(
            request=TaskSerializer,
            responses={
                200:SuccessSerializer,
                400:OpenApiTypes.OBJECT
            }
    )
    def patch(self, request, pk):

        task=self.get_object(
            pk,
            request.user
        )

        serializer=TaskSerializer(instance = task, data = request.data, partial = True)

        if serializer.is_valid():

            serializer.save() 

            return Response({"message":f"Task {pk} updated successfully!"}, status = status.HTTP_200_OK)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

    @extend_schema(
            responses={
                204:SuccessSerializer
            }
    )
    def delete(self, request, pk):

        task=self.get_object(
            pk,
            request.user
        )

        task.delete()

        return Response({"message":"Your task has been deleted."}, status = status.HTTP_204_NO_CONTENT)
        



        
    
    

    
    
