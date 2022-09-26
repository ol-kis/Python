#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
num=input("Enter real number: ")
sum=0
for i in num:
    if not i==".":
        sum=sum+int(i)
print(sum)

