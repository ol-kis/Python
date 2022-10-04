# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:48:00 2022

@author: kiseleva_od
"""

numbers=[0,6,9,7,6,1,0,9,15,80]
b = list(map(str, numbers))
def one(arr):
    
    return [i for i in arr if arr.count(i)==1]
           
print(one(b))





