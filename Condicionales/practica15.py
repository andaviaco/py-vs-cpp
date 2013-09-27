# -*- coding: utf-8 -*-

prom = raw_input("Dame tu promedio: ")
prom = float(prom)

if prom < 0 or prom > 100:
    print "Calificación inválida"
else:
    if prom >= 60:
        print "Aprobaste"
    else:
        print "Reprobaste"