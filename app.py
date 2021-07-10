
from flask import Flask,render_template,request, jsonify
from elasticsearch import Elasticsearch

es_client = Elasticsearch()
app = Flask(__name__)
@app.route('/useradd', methods = ["POST"])
def add_user():
    first_name = request.json.get('fname')
    last_name = request.json.get('lname')
    user_obj = {
        "first_name": first_name,
        "last_name": last_name
    }

    result = es_client.index(index="user-map", body=user_obj)
    return jsonify(result)

@app.route('/userdelete', methods = ["DELETE"])
def delete_user():
    user_name = request.json.get('uname')
    result = es_client.delete()


if __name__ == "__main__":
    app.run(debug=True, port=8000)
