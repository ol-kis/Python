count=0
num=input("enter number: ")
list=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
while count==0:            
    if num.isdigit()==True and int(num)<7 and not int(num)<1:
        if int(num)<6:
            #print("working day")
            print(f' day of the week "{list[int(num)-1]}" is working day')
        else:
            print(f' day of the week "{list[int(num)-1]}" is weekend')

        count=1
    
    else: 
        print("you entered not number or wrong number")
        num=input("enter number again: ")
        
      
        
        
