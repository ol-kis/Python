#Задайте список (словарь не нужно выводить!) из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

from tkinter import N
num = int(input('Enter number: ')) 
arr=list()
for i in range(1,num+1):
    arr.append(round((1+1/i)**i,2))
    #print(arr(i))
print(sum(arr))
print(arr)
