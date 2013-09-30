# -*- coding: utf-8 -*-

mes = 0

'''
for(;mes < 1 || mes > 12;){}

Nunca, para nada se debe implementar un "for" para eso ni de esa manera,
en Python, el "for" no se usa así. Hagamos lo que es correcto:
'''

while mes < 1 or mes > 12:
    mes = int(raw_input("Dame el mes: "))

print "Felicidades"