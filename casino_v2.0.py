#!/usr/bin/env python
# -*- coding: utf-8 -*-

class textColor:
    RESET = '\033[0m'
    BOLD = '\033[01m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    GREY = '\033[90m'


import random
import os

skrita_stevilka = round(random.uniform(1, 30))
print textColor.GREY + "\nZa lažje ugibanje, " + str(skrita_stevilka).rstrip('0').rstrip('.') + " je skrita številka." + textColor.RESET  if '.' in str(skrita_stevilka) else str(skrita_stevilka) + " je skrita številka." + textColor.RESET

poskus = 0

while poskus < 3:
    se_poskus = 3 - poskus
    odgovor = str(raw_input("\nUgani skrito številko med 1 in 30 (poskusiš lahko še " + str(se_poskus) + "x): "))

    if odgovor.isalpha() or len(odgovor) == 0 or " " in odgovor or "+" in odgovor or "-" in odgovor or "*" in odgovor or "/" in odgovor:
        print "\033[91mTo ni število\033[0m"
    elif int(odgovor) == skrita_stevilka:
        os.system('clear')  # dela samo v terminalu za mac in linux!!!
        print textColor.BOLD + textColor. GREEN + "\nČestitamo, " + str(skrita_stevilka).rstrip('0').rstrip('.') + " je pravilni odgovor!" + textColor.RESET if '.' in str(skrita_stevilka) else str(skrita_stevilka) + "je pravilni odgovor!" + textColor.RESET
        os.system('afplay sound.mp3')
        break
    elif poskus == 2:
        print textColor.ORANGE + "\nŽal " + str(odgovor) + " ni pravilen odgovor. Hvala za igro!" + textColor.RESET
        poskus += 1
    else:
        os.system('clear') # dela samo v terminalu za mac in linux!!!
        print textColor.ORANGE + "\nŽal " + str(odgovor) + " ni pravilen odgovor. Prosim poskusite ponovno!" + textColor.RESET
        poskus += 1