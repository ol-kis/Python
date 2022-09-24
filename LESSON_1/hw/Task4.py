quarter_number=input("enter quarter: ")
count=0
while count==0:
    if quarter_number.isdigit()==True and int(quarter_number)<4:
        if int(quarter_number)==1:
            print(f'in {quarter_number} quarter x<0 and y>0')
        elif int(quarter_number)==2:
            print(f'in {quarter_number} quarter x>0 and y>0')
        elif int(quarter_number)==3:
            print(f'in {quarter_number} quarter x>0 and y<0')
        else:
            print(f'in {quarter_number} quarter x<0 and y<0')
        count=1
    else:
            print("you entered not number or number > 4")
            quarter_number=input("enter quarter again: ") 
    
