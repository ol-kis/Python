#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
num=int(input("Enter number: "))
multiplication=1
if num>1:
    for i in range(1,num+1):
        multiplication=multiplication*i
    print(multiplication)
else:
    print("you entered negative number")

