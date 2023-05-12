#!/usr/bin/python3
"""
Start Flask web app listening on port 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    Displays Hello HBNB
    """
    return "Hello HBNB!"


if __name == "__main__":
    app.run(host="0.0.0.0")

