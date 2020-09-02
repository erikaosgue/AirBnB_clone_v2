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


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ display a HTML page: (inside the tag BODY)"""
    dictionary = storage.all(State)
    for state in dictionary.values():
        if id == state.id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.route('/states', strict_slashes=False)
def states():
    """ display a HTML page: (inside the tag BODY)"""
    dictionary = storage.all(State)
    return render_template('9-states.html', dictionary=dictionary)


@app.teardown_appcontext
def teardown(wherever):
    """remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
