# -*- coding: utf-8 -*-

HORA = 6.875

horasTotales = raw_input("Cuántas horas trabajaste en la quincena? ")
horasTotales = float(horasTotales)

salario_normal = horasTotales * HORA
salario_extras = 0

if horasTotales > 80:
	salario_extras = (horasTotales - 80) * HORA * 2
	salario_normal = 80 * HORA

print "Salario normal es: $" + str(salario_normal)
print "Horas extras: $" + str(salario_extras)
print "Total: $" + str(salario_normal + salario_extras)