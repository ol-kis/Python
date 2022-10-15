# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 08:58:07 2022

@author: kiseleva_od
"""
import random

while True:
    try:
        count=int(input("Enter number of count: "))
        number=[(random.randint(1,100)) for x in range(1,count)]
        num_filt=[j for i, j in zip(number, number[1:]) if j > i]
        break
    except ValueError:
        print("You entered not number. Try again! ")
        
print("Source list: "+ (", ").join(map(str,number)))
print("Resuit: "+ (", ").join(map(str,num_filt)))
