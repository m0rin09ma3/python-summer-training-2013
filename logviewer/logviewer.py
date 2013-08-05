#!/usr/bin/env python

import flask

# Create the application.
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

@APP.route('/list')
def listdir():
    folders = os.listdir('../posts')
    return flask.render_template('list.html', folders=folders)

@APP.route('/hello/<name>/')
def hello(name):
    """ Displays the page greets who ever comes to visit it.
    """
    return flask.render_template('hello.html', name=name)

if __name__ == '__main__':
    APP.debug = True
    APP.run()
