# -*- coding: utf-8 -*-
from os import system
from time import sleep

n = 1

while n <= 100:
    '''
    Solo funciona Windows
    if n == 5:
        syste("PAUSE")
    '''
    print str(n) + ":" + str(n) + ":" + str(n)
    n += 1
    sleep(1)
    system("clear")
    # system("CLS") // Windows
