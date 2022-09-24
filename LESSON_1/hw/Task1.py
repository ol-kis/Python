count=0
num=input("enter number: ")
while count==0:            
    if num.isdigit()==True and int(num)<7 and not int(num)<0:
        if int(num)<6:
            print("working day")
        else:
            print("weekend")  
        count=1
    
    else: 
        print("you entered not number or wrong number")
        num=input("enter number again: ")
        
       
        
        