from flask import Flask, jsonify, request, Response
app = Flask(__name__)


todos: list[dict[str, bool]] = [{ "label": "My first task", "done": False }]

@app.route('/myroute', methods=['GET']) 
def hello_world() -> Response:
    return 'Hello World!'

@app.route('/todos', methods=['GET'])
def get_todos() -> Response:
    return jsonify(todos)



@app.route('/todos', methods=['POST'])
def add_new_todo() -> Response:
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position) -> Response:
    print("Será Borrado:", position)

    if position < 0 or position >= len(todos):
        return jsonify({"error": "Posición inválida"}), 400

    todos.pop(position)

    return jsonify(todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)