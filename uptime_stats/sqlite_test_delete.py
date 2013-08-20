#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

if __name__ == "__main__":

    connector = sqlite3.connect("sqlite_test.db")
    cursor = connector.cursor()
    cursor.execute("delete * from uptime1")

    result = cursor.fetchall()

    cursor.close()
    connector.close()

