# -*- coding: utf-8 -*-

# No existe do-while en Python, pero esto es equivalente.
n = 100

while True:
    print n
    n -= 2
    if not n >= 0:
        break

# Hay una mejor solución para esto.
