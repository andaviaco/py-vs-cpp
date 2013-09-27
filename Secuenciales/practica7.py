# -*- coding: utf-8 -*-

from math import sqrt

co = int(raw_input("Dame el cateto opuesto: "))
ca = int(raw_input("Dame el cateto adyacente: "))

print "La hipotenusa es: " + str(sqrt(co*co + ca*ca))