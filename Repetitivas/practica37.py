# -*- coding: utf-8 -*-

GANADOR = 666
cont = 0

# No existe do-while en Python, pero esto es equivalente.
while True:
    n = int(raw_input("Atinale al número: "))
    cont += 1

    if n == GANADOR:
        break

print "Felicidades, le atinaste en " + str(cont) + " intentos"

# Hay una mejor solución para esto