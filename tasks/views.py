from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

from rest_framework.exceptions import PermissionDenied

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)

    def perform_update(self, serializer):
        task = self.get_object()
        # Check if the user is the assigned user (creator or owner of the task)
        if task.assigned_to != self.request.user:
            raise PermissionDenied("You cannot update a task you did not create.")
        serializer.save()

    def perform_destroy(self, instance):
        task = self.get_object()
        # Check if the user is the assigned user (creator or owner of the task)
        if task.assigned_to != self.request.user:
            raise PermissionDenied("You cannot delete a task you did not create.")
        instance.delete()
