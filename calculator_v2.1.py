#!/usr/bin/env python
# -*- coding: utf-8 -*-

class textColor:
    RESET = '\033[0m'
    BOLD = '\033[01m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'

from decimal import Decimal

### kalkulator ###
def kalkulator(prvo_stevilo, operacija, drugo_stevilo):
    if operacija == "+":
        vsota = float(prvo_stevilo) + float(drugo_stevilo)
        print textColor.GREEN + textColor.BOLD + str(prvo_stevilo) + " + " + str(drugo_stevilo) + " = " + (
            str(round(vsota, 3))).rstrip('0').rstrip('.') + textColor.RESET if '.' in (
            str(round(vsota, 3))) else (str(round(vsota, 3))) + textColor.RESET
        return str(prvo_stevilo) + " + " + str(drugo_stevilo) + " = " + (
            str(round(vsota, 3))).rstrip('0').rstrip('.')  if '.' in (
            str(round(vsota, 3))) else (str(round(vsota, 3)))


    elif operacija == "-":
        razlika = float(prvo_stevilo) - float(drugo_stevilo)
        print textColor.GREEN + textColor.BOLD + str(prvo_stevilo) + " - " + str(drugo_stevilo) + " = " + (
            str(round(razlika, 3))).rstrip('0').rstrip('.') + textColor.RESET if '.' in (
            str(round(razlika, 3))) else (str(round(razlika, 3))) + textColor.RESET
        return str(prvo_stevilo) + " - " + str(drugo_stevilo) + " = " + (
            str(round(razlika, 3))).rstrip('0').rstrip('.') if '.' in (
            str(round(razlika, 3))) else (str(round(razlika, 3)))

    elif operacija == "*":
        kolicnik = float(prvo_stevilo) * float(drugo_stevilo)
        print textColor.GREEN + textColor.BOLD + str(prvo_stevilo) + " * " + str(drugo_stevilo) + " = " + (
            str(round(kolicnik, 3))).rstrip('0').rstrip('.') + textColor.RESET if '.' in (
            str(round(kolicnik, 3))) else (str(round(kolicnik, 3))) + textColor.RESET
        return str(prvo_stevilo) + " * " + str(drugo_stevilo) + " = " + (
            str(round(kolicnik, 3))).rstrip('0').rstrip('.') if '.' in (
            str(round(kolicnik, 3))) else (str(round(kolicnik, 3)))


    elif operacija == "/":
        ulomek = float(prvo_stevilo) / float(drugo_stevilo)
        print textColor.GREEN + textColor.BOLD + str(prvo_stevilo) + " / " + str(drugo_stevilo) + " = " + (
            str(round(ulomek, 3))).rstrip('0').rstrip('.') + textColor.RESET if '.' in (
            str(round(ulomek, 3))) else (str(round(ulomek, 3))) + textColor.RESET
        return str(prvo_stevilo) + " / " + str(drugo_stevilo) + " = " + (
            str(round(ulomek, 3))).rstrip('0').rstrip('.') if '.' in (
            str(round(ulomek, 3))) else (str(round(ulomek, 3)))

    else:
        print "Neznana funkcija!"
### END kalkulator ###


### vprašanje ###
history = []
while True:
    racun = raw_input("\nZa izhod pritisni " + textColor.GREEN + textColor.BOLD + "X" + textColor.RESET + ", za zgodovino pritisni " + textColor.GREEN + textColor.BOLD + "H" + textColor.RESET + " za nov račun pritisni " + textColor.GREEN + textColor.BOLD + "katerokoli" + textColor.RESET + " drugo tipko! ")
    if racun == "x" or racun == "x":
        print "Hvala!"
        break
    elif racun == "H" or racun == "h":
        print "Zgodovina dejavnosti:"
        for element in history:
            print textColor.GREEN + textColor.BOLD + element  + textColor.RESET
    else:
        todo_list = []
        ### definicaja spremenljivk ###

        while True:
            prvo = raw_input("Vnesite prvo število: ")
            if prvo.isalpha() or len(prvo) == 0 or " " in prvo:
                print "\033[91mTo ni število\033[0m"
            else:
                todo_list.append(prvo)
                break

        while True:
            znak = raw_input("Vnesi željeno funkcijo (+, -, * ali /): ")
            if not znak in ("+", "-", "*", "/"):
                print "\033[91mNepoznana funkcija\033[0m"
            else:
                todo_list.append(znak)
                break
        while True:
            drugo = raw_input("Vnesite drugo število: ")
            if drugo.isalpha() or len(drugo) == 0 or " " in drugo:
                print "\033[91mTo ni število\033[0m"
            else:
                todo_list.append(drugo)
                break
        ### END definicaja spremenljivk ###

        history_list = kalkulator(todo_list[0], todo_list[1], todo_list[2])
        history.append(history_list)
### END vprašanje ###

