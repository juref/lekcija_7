#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Pozdravljen! \nSem program za pretvorbo kilometrov v milje"

while True:
    answer = raw_input("Želite novo pretvorbo (y/n): ")
    if answer == "y":
        km = raw_input("Prosim vnesi število kilometrov za pretvorbo v milje:")
        print float(km) * 0.621371192
    else:
        print ("hvala!")
        break