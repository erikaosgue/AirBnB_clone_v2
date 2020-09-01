#!/usr/bin/python3
""" starts a Flask web application must:
listening on 0.0.0.0, port 5000
Routes:
* /: display “Hello HBNB!”
* /hbnb: display “HBNB”
* /c/<text>: display “C ”, followed by the value of the text variable
* /python/(<text>): display “Python ”, followed by the value of the text var
    ** The default value of text is “is cool”
* /number/<n>: display “n is a number” only if n is an integer
* /number_template/<n>: display a HTML page only if n is an integer:
    ** H1 tag: “Number: n” inside the tag BODY
* /number_odd_or_even/<n>: display a HTML page only if n is an integer:
    ** H1 tag: “Number: n is even|odd” inside the tag BODY
You must use the option strict_slashes=False in your route definition
Usage: python3 -m web_flask.6-number_odd_or_even
Usage: curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
"""


from flask import Flask
from flask import render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
