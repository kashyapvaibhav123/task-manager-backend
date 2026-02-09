import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from backend.tasks.infrastructure.repositories import TaskRepository
from backend.tasks.services.task_service import TaskService
from backend.tasks.domain.dtos import TaskCreateDTO, TaskUpdateDTO
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
        return Response(
            TaskSerializer(tasks, many=True).data,
            status=status.HTTP_200_OK
        )

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

    def get(self, request, task_id):
        service = get_task_service()
        task = service.get_task(task_id)  # You need this method in your service
        if not task:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)

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
        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)

    def delete(self, request, task_id):
        service = get_task_service()
        service.delete_task(task_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
@method_decorator(csrf_exempt, name="dispatch")
class TaskStatsAPI(APIView):
    def get(self, request):
        service = get_task_service()
        tasks = service.list_tasks()

        stats = {
            "total": len(tasks),
            "todo": sum(1 for t in tasks if t.status == "todo"),
            "inProgress": sum(1 for t in tasks if t.status == "in-progress"),
            "completed": sum(1 for t in tasks if t.status == "completed"),
            "byPriority": {
                "low": sum(1 for t in tasks if t.priority == "low"),
                "medium": sum(1 for t in tasks if t.priority == "medium"),
                "high": sum(1 for t in tasks if t.priority == "high"),
            },
        }
        return Response(stats, status=status.HTTP_200_OK)
@method_decorator(csrf_exempt, name="dispatch")
class WeatherAPI(APIView):
    """
    Fetch current weather for a city (default: Delhi)
    Uses Open-Meteo API
    """
    def get(self, request):
        city = request.query_params.get("city", "Delhi")  # ✅ Default is Delhi
        
        # Coordinates for cities
        city_coords = {
            "Delhi": (28.6139, 77.2090),
            "London": (51.5074, -0.1278),
            "New York": (40.7128, -74.0060),
        }

        lat, lon = city_coords.get(city, city_coords["Delhi"])  # fallback to Delhi

        try:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        except requests.RequestException as e:
            return Response(
                {"error": "Failed to fetch weather", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )