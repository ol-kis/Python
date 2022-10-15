from random import randint
 
print('Введите натуральную степень k:')
k = int(input())
 
def write_file(string):
    with open('FILE2.txt', 'w') as data:
        data.write(string)
 
def create_list(k):
    list = []
    for i in range(k + 1):
        list.append(randint(0, 101))    
    return list
    
def create_str(list):
    wr = ''
    if len(list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += f'{list[i]}x^{len(list) - i - 1}'
                if list [i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                wr += f'{list[i]}x'
                if list[i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                wr += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                wr += ' = 0'
    return wr
 
my_coefficient = create_list(k)
print(create_str(my_coefficient))
write_file(create_str(my_coefficient))