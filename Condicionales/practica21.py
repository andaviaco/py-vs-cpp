# -*- coding: utf-8 -*-

d = int(raw_input("Dame el número de la semana: "))

#No existe switch en Python
if d == 1:
    print "Lun"
elif d == 2:
    print "Mar"
elif d == 3:
    print "Mie"
elif d == 4:
    print "Jue"
elif d == 5:
    print "Vie"
elif d == 6:
    print "Sab"
elif d == 7:
    print "Dom"
else:
    print "error"