# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 08:58:07 2022

@author: kiseleva_od
"""

def f():
    while True:
        try:
            count=int(input("Enter number of count: "))
            num_filt=[x for x in range(20,count+1) if x%20==0 or x%21==0]
            break
        except ValueError:
            print("You entered not number. Try again! ")
        
    print("Resuit: "+ (", ").join(map(str,num_filt)))
f()
