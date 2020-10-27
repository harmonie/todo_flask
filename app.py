from flask import Flask, request, jsonify
import models
import service

app = Flask(__name__)


@app.route("/todo", methods=["POST"])
def create_todo():
    return jsonify(service.ToDoService().create(request.get_json()))

if __name__ == "__main__":
    models.Schema()
    app.run(debug=True)
