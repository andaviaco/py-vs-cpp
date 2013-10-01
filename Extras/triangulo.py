# -*- coding: utf-8 -*-

t = 0
while t < 1 or t > 80:
    t = int(raw_input("Qué tamaño de triángulo quieres?: "))

c = raw_input("Qué caractér quieres que use?: ")

for i in range(t):
    print c * i

for j in range(t, 0, -1):
    print c * j
