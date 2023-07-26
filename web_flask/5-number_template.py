#!/usr/bin/python3
""" Start Flask Web App """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    """return text passed to c/<text>"""
    formatted_text = text.replace('_', " ")
    response = "C {}".format(formatted_text)
    return response


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    formatted_text = text.replace('_', ' ')
    response = "Python {}".format(formatted_text)
    return response


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    response = "{} is a number".format(n)
    return response


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0, port=5000)
