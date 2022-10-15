
import random
count_of_candy=int(2021)
max_count=28


def check(n,m):
    return True if n.isdigit()==True and int(n)<=max_count and int(n)>0 and int(n) <= m else ""
    
def game(a,m):
    print("Welcome to my game: candy")
    player_1=(random.randint(1,2))
    player_2=2 if player_1==1 else 1
    print("Lets start! First stars player number: " + str(player_1))
    dic={1:0,2:0}
    count=1
    candy_have=a
    while candy_have>m:
        if not count%2==0:
            count_candy=input("Player number " + str(player_1)+"! Enter count of candy: ")
            while  not check(count_candy,candy_have)==True:
                count_candy=input("You entered wrong count of candy. Enter count of candy again: ")
            dic[player_1]+=int(count_candy)
            
        else:
            count_candy=input("Player number " + str(player_2)+"! Enter count of candy: ")
            while  not check(count_candy,candy_have)==True:
                count_candy=input("You entered wrong count of candy. Enter count of candy again: ")
            dic[player_2]+=int(count_candy)
        count+=1
        candy_have=a-dic[1]-dic[2]
        print("Now on the table candy: " + str(candy_have))
    win=player_1 if not count%2==0 else player_2
    print("On the table " + str(candy_have) + " candy. It's mean player number " + str(win) + " : you WIN! Congratulations!")    
   
       
        
        
        
game(count_of_candy,max_count)

        
        
    