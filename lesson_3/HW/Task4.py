divisible=input("Enter number: ")
while divisible.isdigit()==False:
    print("You entered not number")
    divisible=input("Enter number again: ")
divisor=2
remainder=1
result=""
while remainder>0:
    result=str(int(divisible)%divisor)+result
    remainder=int(divisible)//divisor
    divisible=remainder
print(result)