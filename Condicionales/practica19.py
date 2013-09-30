# -*- coding: utf-8 -*-

n1 = int(raw_input("Dame el número 1: "))
n2 = int(raw_input("Dame el número 2: "))
n3 = int(raw_input("Dame el número 3: "))

if n1 >= n2:
    m = n1
    if n3 > m:
        m = n3
    else:
        if n3 == m:
            print "Los números son iguales"
elif n2 >= n3:
    m = n2
else:
    m = n3

print "El mayor es " + str(m)