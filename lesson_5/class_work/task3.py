def select(f,a): #данная функция преобразовывает любоую переменную в нужный мне тип
    return [f(x) for x in a]

def read():
    with open("file.txt") as g:
        a=g.readline().split(" ") # вместо того,чтобы каждый раз писать int(),я перевела список в числовой формат
    x=select(int,a)
    return x

def num(x):
    return [(i,i**2) for i in x if i%2==0]
print(num(read()))

