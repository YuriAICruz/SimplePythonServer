from flask import Flask
from flask_api import status
from flask import request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/ok', methods=['GET'])
def return_ok():
    resp = jsonify(success=True, status_code=200, message="200 Ok")
    return resp


@app.route('/data', methods=['POST'])
def receive_data():
    content = request.json
    print(content)

    f = open("D:/logs.txt", "a+")
    f.write(content)

    resp = jsonify(success=True, status_code=200, message="200 Ok")
    return resp


if __name__ == '__main__':
    app.run(host= '0.0.0.0')

# 10.0.2.42
# 10.0.2.42
# 10.0.75.1