from flask import Blueprint, request

bp = Blueprint('names', __name__)


@bp.route('/')
def hello():
    return "Hello World"


@bp.route('/name/<name>')
def hello_name(name):
    return f"Hello {name}"


@bp.route('/name_surname')
def name_surname():
    dct = request.args
    name = dct['name']
    surname = dct['surname']
    return f"Hello {name} {surname}"
