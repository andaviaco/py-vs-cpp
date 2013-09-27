# -*- coding: utf-8 -*-

dinero = raw_input("Cuánto dinero quieres? $")
dinero = int(dinero)

print "Se te entregarán..."

print "$1000 - " + str(dinero/1000)
dinero = dinero % 1000

print "$500 - " + str(dinero/500)
dinero = dinero % 500

print "$200 - " + str(dinero/200)
dinero = dinero % 200

print "$100 - " + str(dinero/100)
dinero = dinero % 100

print "$50 - " + str(dinero/50)
dinero = dinero % 50

print "$20 - " + str(dinero/20)
dinero = dinero % 20

print "$10 - " + str(dinero/10)
dinero = dinero % 10

print "$5 - " + str(dinero/5)
dinero = dinero % 5

print "$2 - " + str(dinero/2)
dinero = dinero % 2

print "$1 - " + str(dinero/1)
dinero = dinero % 1