#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from mymodule.uptime import Uptime

if __name__ == "__main__":

    connector = sqlite3.connect("sqlite_test.db")

    str_uptimes = Uptime()
    for uptime in str_uptimes.split('\n'):
        if uptime: # added this condition statement for '' string
            #print "insert into uptime1 values(%s)" % uptime
            sql = "insert into uptime1 values(%s)" % uptime
            connector.execute(sql)

    connector.commit()
    connector.close()

