#!/usr/bin/env python
# -*- coding: utf-8 -*-


count = 1
number = int(raw_input("Vnesi številko od 1 do 100"))

while count < number < 101:
    if count % 3 == 0 and count % 5 == 0:
        print "fizzbuzz"
        count = count + 1
    if count % 3 == 0:
        print "fizz"
        count = count + 1
    if count % 5 == 0:
        print "buzz"
        count = count + 1
    else:
        print count
        count = count + 1
