# -*- coding: utf-8 -*-

final = 0
primo = False

while final <= 0:
    final = int(raw_input("Da un número positivo: "))

for n in range(2, final + 1):
    div = 2
    while div < n:
        if n % div == 0:
            primo = False #No es primo porque es divisible
            break
        primo = True #Si no fue divisible entonces es primo
        div += 1

    if primo:
        print n