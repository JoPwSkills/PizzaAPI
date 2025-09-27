from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Learn REST APIs", "done": False},
    {"id": 2, "task": "Deploy an app", "done": False}
]

@app.route("/")
def home():
    return {"message": "Welcome to the Simple REST API!"}

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    new_todo = request.json
    new_todo["id"] = len(todos) + 1
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todo.update(request.json)
            return jsonify(todo)
    return {"error": "Todo not found"}, 404

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return {"message": "Todo deleted"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
