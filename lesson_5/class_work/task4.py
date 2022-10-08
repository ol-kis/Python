li=[ x for x in range(1,20)]
li=list(map(lambda x:x+10,li))
print(li)

res = list((filter(lambda x: not x % 2,li)))
print(res)
