from abc import ABC, abstractmethod
from tasks.domain.dtos import TaskCreateDTO, TaskUpdateDTO, TaskStatsDTO

class TaskServiceInterface(ABC):

    @abstractmethod
    def list_tasks(self):
        pass

    @abstractmethod
    def create_task(self, dto: TaskCreateDTO):
        pass

    @abstractmethod
    def update_task(self, task_id: int, dto: TaskUpdateDTO):
        pass

    @abstractmethod
    def delete_task(self, task_id: int):
        pass

    @abstractmethod
    def get_task_stats(self) -> TaskStatsDTO:
        pass
