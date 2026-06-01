
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404


from .models import Task
from .serializers import TaskSerializer


class TaskListCreateAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):

        tasks = Task.objects.filter(
            executer=request.user
        )

        serializer = TaskSerializer(tasks,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):

        serializer=TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(executer=request.user)

            return Response({"message":"Data inserted successfully."},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class TaskDetailAPIView(APIView):
    
    permission_classes=[IsAuthenticated]


    def get_object(self, pk, user):

        return get_object_or_404( Task , pk=pk , executer=user )
    

    def get(self, request, pk):

        task=self.get_object(
            pk,
            request.user
        )

        serializer=TaskSerializer(task)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def patch(self, request, pk):

        task=self.get_object(
            pk,
            request.user
        )

        serializer=TaskSerializer(instance=task,data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save() 

            return Response({"message":f"Task {pk} updated successfully!"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    
    def delete(self,request,pk):

        task=self.get_object(
            pk,
            request.user
        )

        task.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        



        
    
    

    
    
