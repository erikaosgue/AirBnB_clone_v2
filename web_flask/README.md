# 0x04. AirBnB clone - Web framework

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

    What is a Web Framework
    How to build a web framework with Flask
    How to define routes in Flask
    What is a route
    How to handle variables in a route
    What is a template
    How to create a HTML response in Flask by using a template
    How to create a dynamic template (loops, conditions…)
    How to display in HTML data from a MySQL database

# Requirements

## Python Scripts

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the PEP 8 style (version 1.7.*)
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## HTML/CSS Files

    Allowed editors: vi, vim, emacs
    All your files should end with a new line
    A README.md file at the root of the folder of the project is mandatory
    Your code should be W3C compliant and validate with W3C-Validator (except for jinja template)
    All your CSS files should be in the styles folder
    All your images should be in the images folder
    You are not allowed to use !important or id (#... in the CSS file)
    All tags must be in uppercase
    Current screenshots have been done on Chrome 56.0.2924.87.
    No cross browsers

Install Flask
_space $ pip3 install Flask

/* to fix the readme 
space -> space means make a dot
@@ is a sub dot
_space -> make space


## Tasks

[0. Hello Flask!](https://github.com/erikaosgue/AirBnB_clone_v2/blob/master/web_flask/0-hello_route.py)

Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
    @@/: display “Hello HBNB!”
    You must use the option strict_slashes=False in your route definition
    

[1. HBNB](https://github.com/erikaosgue/AirBnB_clone_v2/blob/master/web_flask/1-hbnb_route.py)

Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
    @@/: display “Hello HBNB!”
    @@/hbnb: display “HBNB”
    You must use the option strict_slashes=False in your route definition

[2. C is funy](https://github.com/erikaosgue/AirBnB_clone_v2/blob/master/web_flask/2-c_route.py)
Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
    @@/: display “Hello HBNB!”
    @@/hbnb: display “HBNB”
    @@/c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
    You must use the option strict_slashes=False in your route definition

[3. Python is cool](https://github.com/erikaosgue/AirBnB_clone_v2/blob/master/web_flask/3-python_route.py) 
Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
    @@/: display “Hello HBNB!”
    @@/hbnb: display “HBNB”
    @@/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    @@/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    The default value of text is “is cool”
    You must use the option strict_slashes=False in your route definition)

[4. Is it a number?](https://github.com/erikaosgue/AirBnB_clone_v2/blob/master/web_flask/4-number_route.py)
Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
    @@/: display “Hello HBNB!”
    @@/hbnb: display “HBNB”
    @@/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    @@/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    The default value of text is “is cool”
    @@/number/<n>: display “n is a number” only if n is an integer
    You must use the option strict_slashes=False in your route definition


