#!/usr/bin/python3
""" starts a Flask web application:
listening on 0.0.0.0, port 5000
Routes:
* /states_list: display a HTML page: (inside the tag BODY)
   ** H1 tag: “States”
   ** UL tag: with the list of all State objects present in DBStorage sorted
   by name (A->Z)
    ***LI tag: description of one State: <state.id>: <B><state.name></B> + UL
    tag: with the list of City objects linked to the State sorted by name(A-Z)
        ** LI tag: description of one City: <city.id>: <B><city.name></B>
Terminal 1:
Usage: HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db
python3 -m web_flask.8-cities_by_states
Terminal 2:
curl 0.0.0.0:5000/cities_by_states ; echo ""
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
