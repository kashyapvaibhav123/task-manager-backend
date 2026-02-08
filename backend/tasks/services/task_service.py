class TaskService:

    def __init__(self, repo):
        self.repo = repo

    def list_tasks(self):
        return self.repo.list()

    def create_task(self, dto):
        if not dto.title:
            raise ValueError("Title is required")
        return self.repo.create(dto)

    def update_task(self, task_id, dto):
        return self.repo.update(task_id, dto)

    def delete_task(self, task_id):
        self.repo.delete(task_id)
