#!/usr/bin/python3
""" starts a Flask web application:
listening on 0.0.0.0, port 5000
Routes:
 /hbnb: display a HTML page: (inside the tag BODY)
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """ display a HTML page"""
    dictionary = storage.all(State)
    amenities_dict = storage.all(Amenity)
    place_dict = storage.all(Place)
    return render_template('100-hbnb.html', dictionary=dictionary,
                           amenities_dict=amenities_dict, place_dict=place_dict)


@app.teardown_appcontext
def teardown(wherever):
    """remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
