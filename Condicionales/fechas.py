# -*- coding: utf-8 -*-

fecha = raw_input("Dame la fecha en formato dd:mm:aaaa : ")

#Obtengo el día
d = int(fecha[0:2])
#Obtengo el mes
m = int(fecha[3:5])
#Obtengo el año
a = int(fecha[6:10])

if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    if d < 1 or d > 31:
        print "Fecha inválida"
    else:
        print "Fecha válida"
elif m == 4 or m == 6 or m == 9 or m == 11:
    if d < 1 or d > 30:
        print "Fecha inválida"
    else:
        print "Fecha válida"
elif m == 2:
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        if d < 1 or d > 29:
            print "Fecha inválida"
        else:
            print "Fecha válida"
    elif a > 0:
        if d < 1 or d > 28:
            print "Fecha inválida"
    else:
        print "Fecha inválida"
else:
    print "Fecha inválida"