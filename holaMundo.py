# -*- coding: utf-8 -*-

print "nuevas bases de datos"
variable1 = 29


cadenamultilinea = """
va amaneciendo y no tengo sueno
 pasan las noches y dias enteros
  Soy cocaino no se los niego


"""

print(cadenamultilinea)


a= 10+12
b=2**64
print(b)
print(a)


unatupla = (1,12,22,'holamundo')
print unatupla[3]

unalista = [192,168,12,'ejemplo de lista']
print unalista[3]
unalista.append('agregando un dato a la lista')
print unalista[4]


valor1 = 'nueve'
valor2 = 'diez'

undiccionario = {'id1': valor1, 'id2': valor2}
print undiccionario['id1']
del(undiccionario['id2']) #los diccionarios permiten eliminar cualquier entrada
#estamos haciendo el hola mundo en python
print "En el Ñágara encontré un Ñandú"

var1=0

while var1 <= 2012:
    print "completando", str(var1)
    var1 +=1