# -*- coding: utf-8 -*-

HORA = 6.875

horasTotales = float(raw_input("Cuántas horas trabajaste en la quincena? "))

horasExtras = horasTotales - 80
salario = 80 * HORA
extras = horasExtras * HORA * 2

print "Salario: $" + str(salario)
print "Horas extras: $" + str(extras)
print "Total: $" + str(salario + extras)