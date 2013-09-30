# -*- coding: utf-8 -*-

n = 0

# Podría hacerse simulando el do-while, pero esta es la manera correcta
while n < 1 or n > 15:
    n = int(raw_input("Dame un número del 1 al 15: "))

n / 2 #wtf?...