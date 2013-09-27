# -*- coding: utf-8 -*-

prom = raw_input("Cuál es tu promedio?: ")
prom = float(prom)

if prom < 60:
    print "Estás reprobado"
else:
    print "Aprobaste"

print "Gracias por usar el programa"