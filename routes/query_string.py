from app import app
from flask import request


@app.route('/name_surname')
def name_surname():
    dct = request.args
    name = dct['name']
    surname = dct['surname']
    return f"{name} {surname}"
