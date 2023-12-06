import pdb



def merge(arr):
    if(len(arr)<=1):
        return arr
 
    else:
        mid = len(arr)//2
        left = arr[:mid]
        # pdb.set_trace()
        print("left array = ",left)
 
        right = arr[mid:]
        # pdb.set_trace()
        print("righ array = ",right)
 
 
        left = merge(left)
        right = merge(right)
 
        # pdb.set_trace()
        print(arr)
        return merge_two_sorted_list(left,right,arr)



def merge_two_sorted_list(a,b,arr):
 
    i = j = k = 0

    while(i<len(a) and j<len(b)):
 
        if(a[i]<b[j]):
            arr[k] = a[i]
            i = i+1
            k = k+1
        else:
            arr[k] = b[j]
            j = j+1
            k = k+1
 
    while(i<len(a)):
        arr[k] = a[i]
        i = i+1
        k = k+1
 
    while(j<len(b)):
        arr[k] = b[j]
        j = j+1
        k = k+1
 
    print("array after merging")
    return arr
 
 
 
arr = [2,14,6,8,1,13,5,7]

print(arr)

merge(arr) 
print(arr)   
