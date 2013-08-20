#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
import sqlite3

def sql_select():
    """
    simply fetch all contents from db
    """
    connector = sqlite3.connect("sqlite_test.db")
    cursor = connector.cursor()
    cursor.execute("SELECT DATETIME(datetime,'unixepoch','localtime'), onemnt, fivemnt, fifteenmnt FROM uptime1 ORDER BY datetime")

    result = cursor.fetchall()

    cursor.close()
    connector.close()

    return result

APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """
    http://127.0.0.1:8000
    """
    db_contents = sql_select()
    uptime_data = []
    for row in db_contents:
        datetime = unicode(row[0]) # "2008-05-21 00:00:01"
        date,time = datetime.split(" ")
        year,month,day = date.split("-")
        hour,minute,second = time.split(":")

        # e.g. "[new Date(2008,05,21,00,00,01), 30000, 40645, 123],"
        # google chart counts month from 0, so adjust it to show correct month
        formatted_row = "[new Date(%s,%s,%s,%s,%s,%s),%s,%s,%s]," % (year,int(month)%13-1,day,hour,minute,second,unicode(row[1]),unicode(row[2]),unicode(row[3]))
        
        uptime_data.append(formatted_row)

    return flask.render_template('index.html', uptimes=uptime_data)

if __name__ == '__main__':
    APP.debug = True
    APP.run(port=8000)

