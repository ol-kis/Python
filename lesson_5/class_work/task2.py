# lits=[]
# for i in range(1,101):
#     if i%2==0:
#         print(i)
# # print(list)
def f(x):
    return x**3

def arr():
    # return [i for i in range(1,11) if i%2==0]
    # return [(i,i) for i in range(1,11) if i%2==0]
    return [(i,f(i)) for i in range(1,11) if i%2==0]
print(arr())