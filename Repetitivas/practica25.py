# -*- coding: utf-8 -*-

# No existe do-while en Python, pero esto es equivalente
while True:
	mes = int(raw_input("Dame el mes: "))
	if mes > 1 and mes < 12:
		break

print "Felicidades"