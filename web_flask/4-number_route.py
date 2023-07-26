#!/usr/bin/python3
""" Starts a Flask Web App

App listens on 0.0.0.0:5000
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: displays 'HBNB'
    /c/<text>: displays 'C' followed by <text> value
    /python/<text>: displays 'Python' followed by <text> Value
    /number/<n>: displays 'n is a number' if <n> is an integer
"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Desplays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by <text> value
    Also replaces underscores with spaces
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by <text> value
    Also replaces underscores in <text> with spaces
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' if <n> is an integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
