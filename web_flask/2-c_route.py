#!/usr/bin/python3
""" starts a Flask web application:
* listening on 0.0.0.0, port 5000
* /: display “Hello HBNB!”
* /hbnb: display “HBNB”
* /c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )
Usage: python3 -m web_flask.2-c_route """

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ display “Hello HBNB!” """
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display “HBNB” """
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
    """ display “C <text>” followed by the value of the text variable"""
    new_text = text.replace("_", " ")
    return f"C {escape(new_text)}"


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
