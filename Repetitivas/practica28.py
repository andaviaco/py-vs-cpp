# -*- coding: utf-8 -*-

n =1

# No existe do-while en Python, pero esto es equivalente
while True:
    print n
    n += 1

    if not n <= 100:
        break

# Hay una mejor solución para esto.
