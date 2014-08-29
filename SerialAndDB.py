
"""Este programa tiene que leer una tarjeta rfid desde un microcontrolador
usando el puerto serie, despues tiene que almacenar el id de la tarjeta en
una base de datos.

los campos de la base de datos son:
    rfid    usuario    consumo    dentro    timestamp

"""
#!/usr/bin/env python
#import serial
import MySQLdb

#ser = serial.Serial('/dev/ttyACM0', 9600)
#while True:
#    print ser.readline()


#una forma simple de acceder a una base de datos

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'mysqlroot'
DB_NAME = 'usuarios_CEBUAZ'

def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
#conectar a la base de datos
    conn = MySQLdb.connect(*datos)
#crear un cursor
    cursor = conn.cursor()
#ejecuta una consulta
    cursor.execute(query)

    if query.upper().startwith('SELECT'):
#traer los resultados de un SELECT
        data = cursor.fetchall()
    else:
#hacer efectiva la escritura de datos
        conn.commit()
        data = None

    cursor.close()                        #cerrar el cursor
    conn.close()                          #cerrar el conector


    return data






#insertar datos

dato = raw_input("Dato: ")
query = "INSERT INTO b (b2) VALUES ('%s')" % dato
run_query(query)

#seleccionar todos los registros

query = "SELECT b1, b2 FROM b ORDER BY b2 DESC"
result = run_query(query)
print result

#seleccoinar solo registros conicidentes

criterio = raw_input("Ingrese criterio de busqueda: ")
query = "SELECT b1, b2 FROM b WHERE b2 = '%s'" % criterio
result = run_query(query)
print result


#eliminar registros

criterio = raw_input("Ingrese criterio p7 eliminar coincidencias: ")
query = "DELETE FROM b WHERE b2 = '%s'" % criterio
run_query(query)


#actualizar datos

b1 = raw_input("ID: ")
b2 = raw_input("Nuevo valor: ")
query = "UPDATE b SET b2='%s' WHERE b1 = %i" % (b2, int(b1))
run_query(query)

