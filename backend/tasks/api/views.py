from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from backend.tasks.infrastructure.repositories import TaskRepository
from tasks.services.task_service import TaskService
from tasks.domain.dtos import TaskCreateDTO, TaskUpdateDTO
from .serializers import TaskSerializer


def get_task_service():
    return TaskService(TaskRepository())


@method_decorator(csrf_exempt, name="dispatch")
class TaskListCreateAPI(APIView):
    parser_classes = [JSONParser]
    serializer_class = TaskSerializer

    def get(self, request):
        service = get_task_service()
        tasks = service.list_tasks()
        return Response(TaskSerializer(tasks, many=True).data)

    def post(self, request):
        data = request.data

        dto = TaskCreateDTO(
            title=data.get("title"),
            description=data.get("description", ""),
            status=data.get("status", "todo"),
            priority=data.get("priority", "medium"),
        )

        service = get_task_service()
        task = service.create_task(dto)

        return Response(
            TaskSerializer(task).data,
            status=status.HTTP_201_CREATED
        )


@method_decorator(csrf_exempt, name="dispatch")
class TaskUpdateDeleteAPI(APIView):
    parser_classes = [JSONParser]
    serializer_class = TaskSerializer

    def put(self, request, task_id):
        data = request.data

        dto = TaskUpdateDTO(
            title=data.get("title"),
            description=data.get("description"),
            status=data.get("status"),
            priority=data.get("priority"),
        )

        service = get_task_service()
        task = service.update_task(task_id, dto)

        return Response(TaskSerializer(task).data)

    def delete(self, request, task_id):
        service = get_task_service()
        service.delete_task(task_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
