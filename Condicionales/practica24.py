# -*- coding: utf-8 -*-

m = int(raw_input("Dame el número del mes: "))
d = int(raw_input("Dame el día: "))

if m == 4 or m == 5:
    print "Pimavera"
elif m == 6:
    if d <= 29:
        print "Primavera"
    else:
        print "Verano"

#.
#..
#...
#....
#.....

else:
    print "Mes inválido"