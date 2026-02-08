class TaskCreateDTO:
    def __init__(self, title, description="", status="todo", priority="medium"):
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority


class TaskUpdateDTO:
    def __init__(self, title=None, description=None, status=None, priority=None):
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
