import random 

def check(n):
    return int(n) if int(n)>0 and n.isdigit()==True else ""

def words_list(arr,n):
    return [random.choice(arr) for x in range(1,n)]

def result(arr,n):
    res=list((filter(lambda x: n not in x,arr)))
    return ((" ").join(res))

basa=["абв","авб","бав","бва","ваб","вба"]
srt_word="абв"
replay=input("Enter number of replay: ")

if not isinstance(check(replay),str):
    print("Result of function: " + result(words_list(basa,check(replay)),srt_word))
else:
    print("You enter number < 0")
    