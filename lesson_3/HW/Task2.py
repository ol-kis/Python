numbers=[2, 3, 5, 6] 
def summ_par(arr):
    return [arr[x-1]*arr[-x] for x in range(1,len(arr)-1) ]
print(summ_par(numbers))