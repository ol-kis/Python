# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:59:00 2022

@author: kiseleva_od
"""
coordinates_x=input("enter coordinates x : ")
coordinates_y=input("enter coordinates y : ")
count=0
while count==0:
    if coordinates_x.isdigit()==True and coordinates_y.isdigit()==True:
        if int(coordinates_x)>0:
            if int(coordinates_y)>0:
                print("2 quarter")
            else:
                print("3 quarter")
        else:
            if int(coordinates_y)>0:
                print("1 quarter")
            else:
                print("4 quarter")
        count=1
    else:
        print("you entered not number ")
        coordinates_x=input("enter coordinates x : ")
        coordinates_y=input("enter coordinates y : ")
        
    
    
        
        
        
        
        
