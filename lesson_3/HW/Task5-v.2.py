# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:44:56 2022

@author: kiseleva_od
"""
number=int(input("Enter number: "))

def fib_n(num):
    arr = [0,1]
    for i in range(2, num+1):
        arr.append(arr[-2] - arr[-1])
    arr.reverse() 
    return (arr)
        
def fib_p(num):  
    arr = [0,1]     
    for i in range(2, num+1):
        arr.append(arr[-2] + arr[-1])
    return arr

print(fib_n(number)+fib_p(number)) 




