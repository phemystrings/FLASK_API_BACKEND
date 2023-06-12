from flask import Flask, request
from flask_cors import CORS

from models import create_new, delete_Data, get_all, get_one, update_Data


app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:5500', 'http://127.0.0.1:3000'])


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return get_all()
    elif request.method == 'POST':
        create_new(request.json)
        return {'data': 'New Data Created'}


@app.route('/<id>', methods=('GET', 'PUT', 'DELETE'))
def getOne(id):
    if request.method == 'GET':
        return get_one(id)
    elif request.method == 'PUT':
        return update_Data(id, request.json)
    elif request.method == 'DELETE':
        return delete_Data(id)
