#!/usr/bin/env python
# -*- coding: utf-8 -*-

def convert():
    km = raw_input("\nProsim vnesi število kilometrov za pretvorbo v milje: ")
    convert = float(km) * 0.62137119
    print ("\n" + str(km) + " km je enako " + str(round(convert, 3)) + " mile!\n")

print "Pozdravljen! \n\nSem program za pretvorbo kilometrov v milje"

convert()

while True:
    answer = raw_input("Želite novo pretvorbo (y/n): ")
    if answer == "y":
        convert()
    else:
        print ("\nHvala!")
        break