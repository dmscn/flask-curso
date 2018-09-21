from app import app


@app.route('/')
def hello():
    return "Hello World"


@app.route('/name/<name>')
def hello_name(name):
    return f"Hello {name}"
