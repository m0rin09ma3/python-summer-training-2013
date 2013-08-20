#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

if __name__ == "__main__":

    connector = sqlite3.connect("sqlite_test.db")
    cursor = connector.cursor()
    cursor.execute("select datetime(datetime,'unixepoch','localtime'), onemnt, fivemnt, fifteenmnt from uptime1 order by datetime")

    result = cursor.fetchall()

    for row in result:
        print "===== Hit! ====="
        print "datetime -- " + unicode(row[0])
        print "1min avg -- " + unicode(row[1])
        print "5min avg -- " + unicode(row[2])
        print "15min avg -- " + unicode(row[3])

    cursor.close()
    connector.close()

