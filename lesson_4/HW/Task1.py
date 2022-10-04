# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:40:46 2022

@author: kiseleva_od
"""

num_Pi=3.1415926535897932384626433832795
def enter_num():
    num=input("Enter number: ")
    while num.isdigit()==False:
        print("You entered not number")
        num=input("Enter number again: ")
    return int(num)

def Pi_round(num):
    return round(num_Pi,num)

print(Pi_round(enter_num()))


    