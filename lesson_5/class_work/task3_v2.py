# def read():
#     with open("file.txt") as g:
#         a=g.readline().split(" ") 
#     x=list(map(int,a)) #преобразование строки в число
#     return x

# def num(x):
#     return [(i,i**2) for i in x if i%2==0]
# print(num(read()))

data='1 2 3 4 5 6 7 8 9 10'.split()
res=map(int,data)
res=filter(lambda x: not x % 2,res)
res=list(map(lambda x: (x,x**2),res))
print(res)

