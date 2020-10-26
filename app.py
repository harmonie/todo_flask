from flask import Flask, request
import models
import service

app = Flask(__name__)

@app.route("/todo", methods=["POST"])
def create_todo():
    return service.ToDoService().create(request.get_json())

if __name__ == "__main__":
    models.Schema()
    app.run(debug = True)