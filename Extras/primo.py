# -*- coding: utf-8 -*-

n = 0
while n < 1:
    n = int(raw_input("Dame un número: "))
    if n < 1:
        print "Número inválido"

if n == 1:
    print str(n) + " NO es un número primo"
else:
    for i in range(2, n+1):
        if n % i == 0:
            if n != i:
                print str(n) + " NO es un número primo"
                break
            else:
                print str(n) + " SI es un número primo"