import json
from flask import Flask, request

api = Flask(__name__)

@api.route("/api/v1/health", methods=['GET'])
def get_status():
    msg = '{"health": "up"}'
    j = json.loads(msg)

    return j

@api.route("/api/v1/keys", methods=['POST'])
def handle_post():
    print(request.get_data())

    return ""

if __name__ == "__main__":
    api.run(host='0.0.0.0', debug=True, port=10000)



