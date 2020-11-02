from flask import Flask, request, jsonify, abort
import models
import service

app = Flask(__name__)


@app.route("/todo", methods=["POST"])
def create_todo():
    return jsonify(service.ToDoService().create(request.get_json()))


@app.route("/todo", methods=["GET"])
def get_all_todo():
    return jsonify(service.ToDoService().get_all())

@app.route("/todo/<_id>", methods=["GET"])
def get_by_id(_id):
    todo = service.ToDoService().get_by_id(_id)
    if todo is None:
        abort(404)
    return jsonify(todo)

if __name__ == "__main__":
    models.Schema()
    app.run(debug=True)
