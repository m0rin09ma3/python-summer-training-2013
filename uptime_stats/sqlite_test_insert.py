#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

if __name__ == "__main__":
    connector = sqlite3.connect("sqlite_test.db")

    sql = "insert into uptime1 values(datetime('now'), 2.20, 0.02, 0.22)"
    connector.execute(sql)

    connector.commit()
    connector.close()

