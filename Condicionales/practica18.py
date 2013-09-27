# -*- coding: utf-8 -*-

n1 = float(raw_input("Dame el primer número: "))
n2 = float(raw_input("Dame el segundo número: "))

if n1 > n2:
    print str(n1) + " es mayor que " + str(n2)
else:
    if n2 > n1:
        print str(n2) + " es mayor que " + str(n1)
    else:
        print "Los números son iguales"