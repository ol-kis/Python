
arr=[2, 3, 5, 9, 3]
def summa(arr):
    summ=0
    for i in range(1, len(arr),2):
        summ=summ+arr[i]
    return summ
print(summa(arr))
    