#!/usr/bin/python3
""" starts a Flask web application:
listening on 0.0.0.0, port 5000
Routes:
 /states_list: display a HTML page: (inside the tag BODY)
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ display a HTML page: (inside the tag BODY)"""
    dictionary = storage.all(State)
    return render_template('8-cities_by_states.html', dictionary=dictionary)


@app.teardown_appcontext
def teardown(wherever):
    """remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
