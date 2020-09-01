#!/usr/bin/python3
""" script that starts a Flask web application:
* listening on 0.0.0.0, port 5000
* /: display “Hello HBNB!”
* /hbnb: display “HBNB”
Usage: python3 -m web_flask.1-hbnb_route """

from flask import Flask

app_1 = Flask(__name__)


@app_1.route('/', strict_slashes=False)
def hello_hbnb():
    """ display “Hello HBNB!” """
    return("Hello HBNB!")


@app_1.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display “HBNB” """
    return("HBNB")


if __name__ == "__main__":
    app_1.run("0.0.0.0", 5000)
