# -*- coding: utf-8 -*-

PRECIOBIROTE = 4.5
PRECIOFRIJOl = 15.0
PRECIOQUESO = 65.0
IVA = 16.0

cant_birotes = int(raw_input("Cuántos birotes quieres? "))
cant_frijoles = int(raw_input("Cuántos botes de frijoles quieres? "))
cant_queso = int(raw_input("Cuántos gramos de queso quieres? "))

subtotal = (cant_birotes*PRECIOBIROTE + cant_frijoles*PRECIOFRIJOl
           + cant_queso*(PRECIOQUESO / 1000))

iva = subtotal * (IVA / 100)
total = subtotal + iva

print "Subtotal: $" + str(subtotal)
print "IVA: $" + str(iva)
print "Total: $" + str(total)

pago = float(raw_input("Con cuánto vas a pagar? "))

cambio = pago - total

print "Tu cambio son $" + str(cambio)