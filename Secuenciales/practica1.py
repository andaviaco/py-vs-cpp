# -*- coding: utf-8 -*-

cal1 = raw_input("Ingresa la primera calificación: ")
cal2 = raw_input("Ingresa la segunda calificación: ")
cal3 = raw_input("Ingresa la tercera calificación: ")
cal1 = float(cal1)
cal2 = float(cal2)
cal3 = float(cal3)


promedio = (cal1 + cal2 + cal3) / 3

print "Tu promedio es: " + str(promedio)