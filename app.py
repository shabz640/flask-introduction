from flask import Flask,render_template,request, jsonify
from elasticsearch import Elasticsearch
from read_config import ReadConfig

config_file = "config_file.conf"

config = ReadConfig(config_file)
index_name = config.get_config("config", "index_name")
host_name = config.get_config("config", "hostname")
port = config.get_config("config", "port")

es_client = Elasticsearch([host_name])
app = Flask(__name__)
@app.route('/useradd', methods = ["POST"])
def add_user():
    first_name = request.json.get('fname')
    last_name = request.json.get('lname')
    age = request.json.get('age')
    user_obj = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }

    result = es_client.index(index=index_name, body=user_obj)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=port)
