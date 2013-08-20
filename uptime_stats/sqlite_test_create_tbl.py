#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

if __name__ == "__main__":
    connector = sqlite3.connect("sqlite_test.db")

    sql = """
          CREATE TABLE uptime1(
               datetime   DATETIME,
               onemnt     DECIMAL,
               fivemnt    DECIMAL,
               fifteenmnt DECIMAL
          );"""
    print sql
    connector.execute(sql)
    connector.commit()
    connector.close()
