from uuid import uuid4
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'hello': 'world'})


@app.route('/user', methods=['POST'])
def add_user():
    return jsonify({'id': uuid4()}), 201


if __name__ == '__main__':
    app.run(debug=True)
