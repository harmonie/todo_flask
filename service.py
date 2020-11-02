from models import ToDoModel


class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        return self.model.create(params)

    def get_all(self):
        return self.model.get_all()

    def get_by_id(self, _id):
        return self.model.get_by_id(_id)