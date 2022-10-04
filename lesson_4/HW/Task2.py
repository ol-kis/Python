# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:48:00 2022

@author: kiseleva_od
"""
import math

natur_num=int(input("Enter number: "))
start_d=2
arr=[]
    
def II(num,d):
    while num>1:
        if num%d==0:
            arr.append(d)
            num=num//d
            print(num)
        elif num%(d+1)==0:
                arr.append(d+1)
                num=num//(d+1)       
                print(num)
        else:
            if math.sqrt(num)%1==0:
                arr.append(int(math.sqrt(num)))
            else:
                arr.append(num)
            num=0
    if len(arr)>2:
        return arr
    else:
       arr.insert(0,1)
       return arr
           
                
    

print(II(natur_num,start_d))



        
    
        
    






