# from math import gamma


# def f(x):
#    return x**2
# g=f
# print(f(5))
# print(g(5))


# def calc(x):
#     return x*10

# def math(op,x):
#     print(op(x))

# math(calc,10)


# def sum(x,y):
#     return x+y

# sum=lambda q,w:q+w

def mult(x,y):
    return x*y
    
def calc(op,a,b):
    print(op(a,b))

calc(mult,4,5)
calc(lambda q,w:q+w,4,5)




