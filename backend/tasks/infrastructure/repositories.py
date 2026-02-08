from tasks.models import Task

class TaskRepository:

    def list(self):
        return Task.objects.all().order_by("-created_at")

    def create(self, dto):
        return Task.objects.create(
            title=dto.title,
            description=dto.description,
            status=dto.status,
            priority=dto.priority,
        )

    def update(self, task_id, dto):
        task = Task.objects.get(id=task_id)

        if dto.title is not None:
            task.title = dto.title
        if dto.description is not None:
            task.description = dto.description
        if dto.status is not None:
            task.status = dto.status
        if dto.priority is not None:
            task.priority = dto.priority

        task.save()
        return task

    def delete(self, task_id):
        Task.objects.filter(id=task_id).delete()
