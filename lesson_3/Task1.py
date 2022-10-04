# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:15:43 2022

@author: kiseleva_od
"""

num=int(input("Enter number: "))
arr=[]
for i in range(-num,num+1):
    arr.append(i)
print(arr)

data=open("file.txt","r")
for line in data:
    print(arr[int(line)])
data.close