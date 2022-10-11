# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:41:55 2022

@author: kiseleva_od
"""
import random
count_of_candy=int(2021)
max_count=28


def check(n,m):
    return True if n.isdigit()==True and int(n)<=max_count and int(n)>0 and int(n) <= m else ""
    
def game(a,m):
    print("Welcome to my game: candy")
    player_1=(random.randint(1,2)) #player number 2 - bot
    #player_2=2 if player_1==1 else 1
    move="man" if player_1==1 else "bot"
    print("Lets start! First stars player number: " + str(player_1))
    dic={1:0,2:0}
    candy_have=a
    while candy_have>m:
        if move=="man":
            count_candy=input("Player! Enter count of candy: ")
            while  not check(count_candy,candy_have)==True:
                count_candy=input("You entered wrong count of candy. Enter count of candy again: ")
            dic[1]+=int(count_candy)
            move="bot"
        else:
            bot_move=random.randint(0,29)
            dic[2]+=bot_move
            print("Bot enter: "+str(bot_move))
            move="man"
        candy_have=a-dic[1]-dic[2]
        print("Now on the table candy: " + str(candy_have))
    win="bot" if  move=="bot" else "man"
    print("Now on the table " + str(candy_have) + " candy. It's mean "+ win+" WIN! Congratulations!")    
   
        
        
game(count_of_candy,max_count)

        
        
    