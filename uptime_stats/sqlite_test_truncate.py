#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

if __name__ == "__main__":

    connector = sqlite3.connect("sqlite_test.db")
    connector.execute("delete from uptime1")
    connector.commit()
    connector.close()

