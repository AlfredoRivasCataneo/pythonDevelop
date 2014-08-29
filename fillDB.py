#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

from random import randint
import sys
import time
import datetime



con = mdb.connect('localhost', 'root', 'neverday', 'parapruebas');
archivo = open('usuarios.txt','w')

rfid = [0xff, 0xff, 0xff, 0xff, 0xff]
usuario = [rfid]
#print ('usuario', usuario)
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Pasajeros")
    cur.execute("CREATE TABLE Pasajeros(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 rfiduser VARCHAR(25))")
    cur.execute("ALTER TABLE Pasajeros ADD email VARCHAR(60) AFTER rfiduser")
    cur.execute("INSERT INTO Pasajeros(rfiduser) VALUES('prueba rifd')")




    for x in range (0, 10000):
        #print('\n')
        for i in range (0, 5):
            rfid[i]= hex(randint(0, 255))

        cur.execute("INSERT INTO Pasajeros(rfiduser, email) VALUES('prueba rifd', 'ajua@nasa.com')")
        #cur.execute("INSERT INTO Pasajeros(email) VALUES('ajua@nasa.com')")
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        usuario.append(rfid)
        #print('usuario ',x,usuario[x])
        archivo.write("usuario \t")
        archivo.write(str(x))
        archivo.write("\t")
        archivo.write(str(st))
        archivo.write("\t")
        #archivo.write(str(usuario[x]))
        archivo.write("\n")

archivo.close()