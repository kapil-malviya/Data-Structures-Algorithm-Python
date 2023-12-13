def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


# arr = [4, 8, 3, 2, 1]
arr = [10,1,7,4,10,-8,2,11]
insertion_sort(arr)
print(arr)



'''

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        for j in range(i-1, -1, -1):
            if key < arr[j]:
                arr[j+1] = arr[j]
                arr[j] = key



# arr = [4, 8, 3, 2, 1]
arr = [10, 1, 7, 4, 10, 8, 2, 11]
insertion_sort(arr)
print(arr)


'''
