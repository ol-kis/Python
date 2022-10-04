# numbers=[1.15,9.28,10.98,1.01,2,6.33]
# def max_min(arr):
#     list=[round(arr[x]%1,2) for x in range(0,len(arr))]
#     list.sort()
#     if list[0]==0:
#         return list[-1]-list[1]
#     else:
#         return list[-1]-list[0]
# print(max_min(numbers))


float_list = [1.1, 1.2, 3.1, 5, 10.01]
min_float = 1
max_float = 0

for i in float_list:
    if i % 1 <= min_float and i % 1 != 0:
        min_float = round((i % 1), 2)
    if i % 1 >= max_float and i % 1 != 0:
        max_float = round((i % 1), 2)
        
print('{} - {} = {}'.format(max_float, min_float, (max_float-min_float)))