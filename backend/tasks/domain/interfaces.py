# tasks/domain/interfaces.py

from abc import ABC, abstractmethod

class TaskRepositoryInterface(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, task_id):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, task, data):
        pass

    @abstractmethod
    def delete(self, task):
        pass

    @abstractmethod
    def get_stats(self):
        pass
