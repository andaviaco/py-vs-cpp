# -*- coding: utf-8 -*-
"""
Pedir números y sumarlos mientras no sean negativos
"""

# Similar a do-while
suma = 0
while True:
    n = int(raw_input("Da un número: "))
    if n >= 0:
        suma = suma + n
    
    if n < 0:
        break

print "La suma total fue: " + str(suma)


# Con while
suma = 0
while suma < 50:
    n = int(raw_input("Da un número: "))
    if n >= 0:
        suma = suma + n

print "La suma total fue: " + str(suma)

# Con for
# Este tipo de cosas no se hacen con for, nunca.