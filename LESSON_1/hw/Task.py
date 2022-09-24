# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:59:00 2022

@author: kiseleva_od
"""
coordinates_x=input("enter coordinates x : ")
coordinates_y=input("enter coordinates y : ")
if not (coordinates_x.isdigit()==True or coordinates_y.isdigit()==True):
    while not (coordinates_x.isdigit()==True and coordinates_y.isdigit()==True):
        print("you entered not number ")
        coordinates_x=input("enter coordinates x : ")
        coordinates_y=input("enter coordinates y : ")
if int(coordinates_x)>0:
    if int(coordinates_y)>0:
        print("2 quarter")
    else:
        print("4 quarter")
else:
    if int(coordinates_y)>0:
        print("1 quarter")
    else:
        print("3 quarter")