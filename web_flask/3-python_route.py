#!/usr/bin/python3
""" starts a Flask web application:
* listening on 0.0.0.0, port 5000
routes:
* /: display “Hello HBNB!”
* /hbnb: display “HBNB”
* /c/<text>: display “C ”, followed by the value of the text variable
* /python/(<text>): display “Python ”, followed by the value of the text var
Usage: python3 -m web_flask.3-python_route """


from flask import Flask

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
    return "C {}".format(new_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ display “Python ”, followed by the value of the text variable """
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
