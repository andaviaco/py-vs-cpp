# -*- coding: utf-8 -*-
"""
Pedir números mientras la suma no sea 50
"""

suma = 0

# Similar a do-while
while True:
    n = int(raw_input("Da un número: "))
    suma = suma + n
    
    if not suma < 50:
        break


# Con while
while suma < 50:
    n = int(raw_input("Da un número: "))
    suma = suma + n


# Con for
'''
for (; suma<50; )

Esto no se hace nunca en Python.
Si lo haces te puede provocar una enfermedad mental, 
la mejor (única) opción es usar while
'''