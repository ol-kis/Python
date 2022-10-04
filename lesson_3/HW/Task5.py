# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:44:56 2022

@author: kiseleva_od
"""
num=int(input("Enter number: "))
def fib(arr):
    x = [0,1]
    for i in range(2, num+1):
        x.append(x[-2] - x[-1])
        x.reverse()
    x2 = [0,1]
    for i in range(2, num+1):
            x2.append(x2[-2] + x2[-1])

    x2.pop(0)
print(', '.join(str(y) for y in x+x2))
