#!/usr/bin/env python
# -*- coding: utf-8 -*-


number = int(raw_input("Vnesi številko od 1 do 100: "))

### prva verzija ###
# count = 1
# while count < number + 1:
#     if count % 3 == 0 and count % 5 == 0:
#         print "fizzbuzz"
#         count += 1
#     elif count % 3 == 0:
#         print "fizz"
#         count += 1
#     elif count % 5 == 0:
#         print "buzz"
#         count += 1
#     else:
#         print count
#         count += 1
        
# ### še en način ###
# for x in range(number):
#     y = x + 1
#     if y % 3 == 0 and y % 5 == 0:
#         print "fizzbuz"
#     elif y % 3 == 0:
#         print "fizz"
#     elif y % 5 == 0:
#         print "buzz"
#     else:
#         print y

### še drug način ###
for y in range(1, number + 1):
    if y % 3 == 0 and y % 5 == 0:
        print "fizzbuz"
    elif y % 3 == 0:
        print "fizz"
    elif y % 5 == 0:
        print "buzz"
    else:
        print y