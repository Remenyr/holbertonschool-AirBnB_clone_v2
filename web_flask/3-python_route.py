#!/usr/bin/python3
""" Flask: Adding default input """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)