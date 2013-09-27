# -*- coding: utf-8 -*-

prom = raw_input("Cuál es tu promedio?: ")
prom = float(prom)

if prom >= 95:
    prom = 100

print "Tu promedio es " + str(prom)