#!/usr/bin/env python

import flask
import os

# Create the application.
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    logs = os.listdir('./posts')
    return flask.render_template('index.html', logs=logs)

@APP.route('/list/<json>/')
def list(json):
    """ Displays the page greets who ever comes to visit it.
    """
    with open('./posts/' + json) as f:
        lines = f.readlines()
    return flask.render_template('list.html', data=lines)

if __name__ == '__main__':
    APP.debug = True
    APP.run()
