#!/usr/bin/python3
"""starts FLask Web App

App listens on 0.0.0.0:5000
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays "HBNB'
    /c/<text>: Displays 'C' folowed by <text>
    /python/<text>: displays "Python' followed by <text> value
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by <text> value"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is collo"):
    """Displays 'Python' followed by <text> value
    Also replaces any underscores with slashes
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
