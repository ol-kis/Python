def read():
    with open("text_words.txt") as g:
         str_w=list(g.readline())
    return str_w

def word_unique(arr):
    return [arr[x] for x in range(0,len(arr)-1) if not arr[x]== arr[x+1]]

def count_repeat(arr1,arr2):
    help=0
    res=""
    for x in range(0,len(arr1)):
        count=0
        for y in range(help,len(arr2)):
            if arr1[x]== arr2[y]:
                count+=1
            else:
                if not count==0:
                    break
        help+=count
        res+=str(count)+arr1[x]
    return res

def write():
    with open("text_code_words.txt",'w') as g:
        x=count_repeat(word_unique(read()),read())
        g.writelines(x)
    
write()

# 5a29v4s3D3d2F4g2O3i2a1
#aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa