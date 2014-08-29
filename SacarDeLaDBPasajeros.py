#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'neverday', 'parapruebas');

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Pasajeros")

    rows = cur.fetchall()

    for row in rows:
        print row