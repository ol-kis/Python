# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:48:00 2022

@author: kiseleva_od
"""

numbers=["йцу", "фыв", "ячс", "цук", "йцукен"]
string="йцу"
def entry(arr,m):
    a=[items for items in range(0,len(arr)) if m ==arr[items]]
    return a[1]+1 if len(a)==2 else "Нет второго вхождения"
            
          
print(entry(numbers,string))






