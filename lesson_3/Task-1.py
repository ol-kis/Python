# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:41:46 2022

@author: kiseleva_od
"""
#запись данных
# data=open("file.txt","a") #a-добавление новых данных, w -перезапись
# data.writelines("Привет")
# data.write("\nПривет13\n")
# data.close()

#запись данных

# with open ("file.txt","a") as data:
#     data.write("\nПривет13\n")

#чтение данных
path="file.txt"
data=open(path,"r")

for line in data:
    print(line)
data.close
    
    
