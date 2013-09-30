# -*- coding: utf-8 -*-

m = int(raw_input("Dame el número del mes: "))

if m == 1 or m == 2 or m == 3:
    print "1er trimestre"
elif m == 4 or m == 5 or m == 6:
    print "2do trimestre"
elif m == 7 or m == 8 or m == 9:
    print "3er trimestre"
elif m == 10 or m == 11 or m == 12:
    print "4to trimestre"
else:
    print "Mes inválido"
