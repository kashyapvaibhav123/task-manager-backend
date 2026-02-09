# from django.urls import path
# from .views import (
#     TaskListCreateAPI,
#     TaskUpdateDeleteAPI,
#     TaskStatsAPI
# )

# urlpatterns = [
#     path("tasks/", TaskListCreateAPI.as_view()),
#     path("tasks/<int:task_id>/", TaskUpdateDeleteAPI.as_view()),
#     path("tasks/stats/", TaskStatsAPI.as_view()),
# ]



from django.urls import path
from .views import TaskListCreateAPI, TaskUpdateDeleteAPI,TaskStatsAPI,WeatherAPI

urlpatterns = [
    path("tasks/", TaskListCreateAPI.as_view()),
    path("tasks/<int:task_id>/", TaskUpdateDeleteAPI.as_view()),
    path("tasks/stats/", TaskStatsAPI.as_view(), name="task-stats"),
    path("weather/", WeatherAPI.as_view(), name="weather-api"),

]

