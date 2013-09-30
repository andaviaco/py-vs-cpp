# -*- coding: utf-8 -*-

# Podría hacerse simulando el do-while, pero esta es la manera correcta
totalTablas = 0
nMultp = 0

while totalTablas <= 0:
    totalTablas = int(raw_input("Cuántas tablas quieres?: "))
    
while nMultp <= 0:
    nMultp = int(raw_input("Hasta qué número quieres multiplicar?: "))

for nt in range(1, totalTablas + 1):
    for m in range(1, nMultp + 1):
        print "{} × {} = {}".format(nt, m, nt*m) #String formatting recomendado
        #print str(nt) + " × " + str(m) + " = " + str(nt * m)
    print ""