#!/usr/bin/env python
# -*- coding: utf-8 -*-

class textColor:
    RESET = '\033[0m'
    BOLD = '\033[01m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'


### funkcija račun ###
def operacija(x, znak, y):
    if znak == "+":
        izracun = float(x) + float(y)
    elif znak == "-":
        izracun = float(x) - float(y)
    elif znak == "*":
        izracun = float(x) * float(y)
    elif znak == "/":
        izracun = float(x) / float(y)
    print textColor.GREEN + textColor.BOLD + str(x) + " + " + str(y) + " = " + (str(round(izracun, 3))).rstrip('0').rstrip('.') + textColor.RESET if '.' in (
        str(round(izracun, 3))) else (str(round(izracun, 3))) + textColor.RESET
    return str(x) + " + " + str(y) + " = " + (
        str(round(izracun, 3))).rstrip('0').rstrip('.') if '.' in (str(round(izracun, 3))) else (str(round(izracun, 3)))
### END funkcija račun ###

def kalkulator():

    while True:
        racun = raw_input("\nZa izhod pritisni " + textColor.GREEN + textColor.BOLD + "X" + textColor.RESET + ", za zgodovino pritisni " + textColor.GREEN + textColor.BOLD + "H" + textColor.RESET + " za nov račun pritisni " + textColor.GREEN + textColor.BOLD + "katerokoli" + textColor.RESET + " drugo tipko! ")
        if racun == "x" or racun == "x":
            print "Hvala!"
            break
        elif racun == "H" or racun == "h":
            print "Zgodovina dejavnosti:"
            for element in history:
                print textColor.GREEN + textColor.BOLD + element + textColor.RESET
        else:
            todo_list = []
            while True:
                stevilo = raw_input("Vnesite stevilo število: ")
                if stevilo.isalpha() or len(
                        stevilo) == 0 or " " in stevilo or "+" in stevilo or "-" in stevilo or "*" in stevilo or "/" in stevilo:
                    print "\033[91mTo ni število\033[0m"
                else:
                    todo_list.append(stevilo)
                    break

            while True:
                znak = raw_input("Vnesi željeno funkcijo (+, -, * ali /): ")
                if not znak in ("+", "-", "*", "/"):
                    print "\033[91mNepoznana funkcija\033[0m"
                else:
                    todo_list.append(znak)
                    break

            while True:
                stevilo = raw_input("Vnesite stevilo število: ")
                if stevilo.isalpha() or len(
                        stevilo) == 0 or " " in stevilo or "+" in stevilo or "-" in stevilo or "*" in stevilo or "/" in stevilo:
                    print "\033[91mTo ni število\033[0m"
                else:
                    todo_list.append(stevilo)
                    break
            history_list = operacija(todo_list[0], todo_list[1], todo_list[2])
            history.append(history_list)

history = []
kalkulator()