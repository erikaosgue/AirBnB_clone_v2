#!/usr/bin/python3
""" script that starts a Flask web application:
from the root folder AirBnB_v2 run
Usage: python3 -m web_flask.0-hello_route"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ used to generate URLs for this particular function, and returns the
    message we want to display in the user’s browser."""
    return ('Hello HBNB!')


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
