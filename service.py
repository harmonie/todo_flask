import models

class ToDoService:
    def __int__(self):
        self.model = models.ToDoModel()

    def create(self, params):
        return self.model.create(params["text"], params["Description"])