class Task:
    _id_counter = 1

    def __init__(self, title: str, description: str):
        self.id = Task._id_counter
        self.title = title
        self.description = description
        self.completed = False
        Task._id_counter += 1

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, completed={self.completed})"
