# -*- coding: utf-8 -*-

res = 0
num1 = raw_input("Da el primer multiplicador: ")
num2 = raw_input("Da el segundo multiplicador: ")

tam1 = len(num1)
tam2 = len(num2)

for i in range(tam1):
    n1 = int(num1[i:i+1])

    for j in range(tam2):
        n2 = int(num2[j:j+1])
        res += n1 * n2

print res